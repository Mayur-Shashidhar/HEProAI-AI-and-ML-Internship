"""
Activity 4: Mentor Matching & Intervention Recommendations
Author: Student Mentoring System
Date: February 2026

This module implements intelligent mentor-student matching based on:
- Student needs (academic, wellness, career)
- Mentor expertise and availability
- Risk level assessment
- Intervention recommendations
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


class MentorMatchingSystem:
    """
    A comprehensive system for matching students with mentors
    and generating intervention recommendations.
    """
    
    def __init__(self, students_file, mentors_file):
        """
        Initialize the matching system with student and mentor data.
        
        Parameters:
        -----------
        students_file : str
            Path to the students CSV file
        mentors_file : str
            Path to the mentors CSV file
        """
        self.students = pd.read_csv(students_file)
        self.mentors = pd.read_csv(mentors_file)
        self.recommendations = None
        self.high_risk_alerts = []
        
    def identify_student_needs(self, student):
        """
        Identify the primary needs of a student based on their scores.
        
        Parameters:
        -----------
        student : pandas.Series
            Student data row
            
        Returns:
        --------
        dict : Dictionary containing need priorities and scores
        """
        needs = {
            'academic': 100 - student['academic_score'],
            'wellness': 100 - student['wellness_score'],
            'career': 100 - student['career_readiness']
        }
        
        # Determine primary need (highest deficit)
        primary_need = max(needs, key=needs.get)
        
        return {
            'primary_need': primary_need,
            'needs_scores': needs,
            'urgency': self._calculate_urgency(student)
        }
    
    def _calculate_urgency(self, student):
        """
        Calculate the urgency level for student intervention.
        
        Parameters:
        -----------
        student : pandas.Series
            Student data row
            
        Returns:
        --------
        str : Urgency level (Critical, High, Medium, Low)
        """
        # Calculate overall risk score
        risk_factors = {
            'low_gpa': 1 if student['gpa'] < 2.0 else 0,
            'low_attendance': 1 if student['attendance'] < 60 else 0,
            'low_completion': 1 if student['assignment_completion'] < 60 else 0,
            'high_stress': 1 if student['stress_level'] in ['High', 'Very High'] else 0,
            'at_risk_cluster': 1 if student['cluster'] == 'At_Risk' else 0
        }
        
        risk_score = sum(risk_factors.values())
        
        if risk_score >= 4:
            return 'Critical'
        elif risk_score >= 3:
            return 'High'
        elif risk_score >= 2:
            return 'Medium'
        else:
            return 'Low'
    
    def match_mentor(self, student, needs_analysis):
        """
        Match a student with the most suitable mentor.
        
        Parameters:
        -----------
        student : pandas.Series
            Student data row
        needs_analysis : dict
            Student needs analysis
            
        Returns:
        --------
        pandas.Series or None : Matched mentor data
        """
        primary_need = needs_analysis['primary_need']
        
        # Map needs to mentor types
        need_to_mentor_type = {
            'academic': 'Academic',
            'wellness': 'Wellness',
            'career': 'Career'
        }
        
        required_mentor_type = need_to_mentor_type[primary_need]
        
        # Filter available mentors by type
        available_mentors = self.mentors[
            self.mentors['mentor_type'] == required_mentor_type
        ].copy()
        
        if available_mentors.empty:
            return None
        
        # Score mentors based on availability and expertise match
        available_mentors['match_score'] = 0
        
        # Availability scoring
        availability_scores = {'High': 3, 'Medium': 2, 'Low': 1}
        available_mentors['match_score'] += available_mentors['availability'].map(availability_scores)
        
        # For academic mentors, check major compatibility
        if required_mentor_type == 'Academic':
            student_major = student['major']
            # Simple keyword matching
            for idx, mentor in available_mentors.iterrows():
                if any(keyword in mentor['specialization'] for keyword in student_major.split()):
                    available_mentors.at[idx, 'match_score'] += 2
        
        # Prefer more experienced mentors for high-urgency cases
        if needs_analysis['urgency'] in ['Critical', 'High']:
            available_mentors['match_score'] += available_mentors['experience_years'] / 5
        
        # Select mentor with highest match score
        best_mentor = available_mentors.nlargest(1, 'match_score').iloc[0]
        
        return best_mentor
    
    def generate_intervention(self, student, needs_analysis, mentor):
        """
        Generate specific intervention recommendations.
        
        Parameters:
        -----------
        student : pandas.Series
            Student data row
        needs_analysis : dict
            Student needs analysis
        mentor : pandas.Series
            Matched mentor data
            
        Returns:
        --------
        dict : Intervention recommendations
        """
        primary_need = needs_analysis['primary_need']
        urgency = needs_analysis['urgency']
        
        # Define intervention strategies
        interventions = {
            'academic': {
                'Critical': [
                    'Immediate 1-on-1 tutoring sessions (3x/week)',
                    'Academic probation support plan',
                    'Course load reduction recommendation',
                    'Learning skills workshop enrollment'
                ],
                'High': [
                    'Weekly tutoring sessions (2x/week)',
                    'Study group participation',
                    'Assignment planning support',
                    'Academic skills assessment'
                ],
                'Medium': [
                    'Bi-weekly tutoring sessions',
                    'Study techniques workshop',
                    'Time management training'
                ],
                'Low': [
                    'Monthly check-ins',
                    'Resource recommendations',
                    'Optional study groups'
                ]
            },
            'wellness': {
                'Critical': [
                    'Immediate counseling referral',
                    'Daily check-in protocol',
                    'Stress management intensive program',
                    'Medical leave evaluation if needed'
                ],
                'High': [
                    'Weekly counseling sessions',
                    'Stress reduction workshop',
                    'Peer support group enrollment',
                    'Sleep and wellness assessment'
                ],
                'Medium': [
                    'Bi-weekly wellness check-ins',
                    'Mindfulness workshop',
                    'Work-life balance coaching'
                ],
                'Low': [
                    'Monthly wellness check-ins',
                    'Self-care resources',
                    'Campus wellness activities'
                ]
            },
            'career': {
                'Critical': [
                    'Intensive career counseling (weekly)',
                    'Immediate internship search support',
                    'Resume and LinkedIn overhaul',
                    'Interview skills bootcamp'
                ],
                'High': [
                    'Career planning sessions (bi-weekly)',
                    'Networking event participation',
                    'Job search strategy development',
                    'Professional skills workshop'
                ],
                'Medium': [
                    'Monthly career guidance',
                    'Resume review',
                    'Career fair attendance'
                ],
                'Low': [
                    'Semester career planning',
                    'Industry exploration',
                    'Alumni networking opportunities'
                ]
            }
        }
        
        # Select appropriate interventions
        recommended_actions = interventions[primary_need][urgency]
        
        return {
            'primary_intervention': primary_need.capitalize(),
            'urgency_level': urgency,
            'recommended_actions': recommended_actions,
            'frequency': self._get_meeting_frequency(urgency),
            'duration': self._get_program_duration(urgency)
        }
    
    def _get_meeting_frequency(self, urgency):
        """Get recommended meeting frequency based on urgency."""
        frequency_map = {
            'Critical': 'Daily/3x per week',
            'High': '2x per week',
            'Medium': 'Weekly',
            'Low': 'Bi-weekly or Monthly'
        }
        return frequency_map.get(urgency, 'Monthly')
    
    def _get_program_duration(self, urgency):
        """Get recommended program duration based on urgency."""
        duration_map = {
            'Critical': '1 semester (with intensive support)',
            'High': '1 semester',
            'Medium': '6-8 weeks',
            'Low': '4-6 weeks'
        }
        return duration_map.get(urgency, '1 month')
    
    def create_high_risk_alert(self, student, needs_analysis, mentor, intervention):
        """
        Create an alert for high-risk students.
        
        Parameters:
        -----------
        student : pandas.Series
            Student data row
        needs_analysis : dict
            Student needs analysis
        mentor : pandas.Series
            Matched mentor data
        intervention : dict
            Intervention recommendations
            
        Returns:
        --------
        dict : Alert information
        """
        alert = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'student_id': student['student_id'],
            'student_name': student['name'],
            'urgency': needs_analysis['urgency'],
            'gpa': student['gpa'],
            'attendance': student['attendance'],
            'stress_level': student['stress_level'],
            'assigned_mentor': mentor['name'] if mentor is not None else 'UNASSIGNED',
            'mentor_contact': mentor['contact'] if mentor is not None else 'N/A',
            'immediate_actions': intervention['recommended_actions'][:2],
            'alert_type': 'CRITICAL' if needs_analysis['urgency'] == 'Critical' else 'HIGH_PRIORITY'
        }
        
        return alert
    
    def perform_matching(self):
        """
        Perform complete mentor-student matching process.
        
        Returns:
        --------
        pandas.DataFrame : Complete recommendations table
        """
        recommendations_list = []
        
        for idx, student in self.students.iterrows():
            # Step 1: Analyze student needs
            needs_analysis = self.identify_student_needs(student)
            
            # Step 2: Match with appropriate mentor
            mentor = self.match_mentor(student, needs_analysis)
            
            # Step 3: Generate intervention plan
            intervention = self.generate_intervention(student, needs_analysis, mentor)
            
            # Step 4: Create high-risk alert if needed
            if needs_analysis['urgency'] in ['Critical', 'High']:
                alert = self.create_high_risk_alert(student, needs_analysis, mentor, intervention)
                self.high_risk_alerts.append(alert)
            
            # Step 5: Compile recommendation
            recommendation = {
                'student_id': student['student_id'],
                'student_name': student['name'],
                'cluster': student['cluster'],
                'academic_score': student['academic_score'],
                'wellness_score': student['wellness_score'],
                'career_readiness': student['career_readiness'],
                'gpa': student['gpa'],
                'primary_need': needs_analysis['primary_need'],
                'urgency_level': needs_analysis['urgency'],
                'mentor_id': mentor['mentor_id'] if mentor is not None else 'NONE',
                'mentor_name': mentor['name'] if mentor is not None else 'No Available Mentor',
                'mentor_type': mentor['mentor_type'] if mentor is not None else 'N/A',
                'mentor_expertise': mentor['specialization'] if mentor is not None else 'N/A',
                'intervention_type': intervention['primary_intervention'],
                'meeting_frequency': intervention['frequency'],
                'program_duration': intervention['duration'],
                'action_1': intervention['recommended_actions'][0] if len(intervention['recommended_actions']) > 0 else '',
                'action_2': intervention['recommended_actions'][1] if len(intervention['recommended_actions']) > 1 else '',
                'action_3': intervention['recommended_actions'][2] if len(intervention['recommended_actions']) > 2 else ''
            }
            
            recommendations_list.append(recommendation)
        
        self.recommendations = pd.DataFrame(recommendations_list)
        return self.recommendations
    
    def save_recommendations(self, filename='recommendations.csv'):
        """Save recommendations to CSV file."""
        if self.recommendations is not None:
            self.recommendations.to_csv(filename, index=False)
            print(f"✓ Recommendations saved to {filename}")
        else:
            print("✗ No recommendations to save. Run perform_matching() first.")
    
    def save_alerts(self, filename='high_risk_alerts.csv'):
        """Save high-risk alerts to CSV file."""
        if self.high_risk_alerts:
            alerts_df = pd.DataFrame(self.high_risk_alerts)
            alerts_df.to_csv(filename, index=False)
            print(f"✓ High-risk alerts saved to {filename}")
        else:
            print("✗ No high-risk alerts to save.")
    
    def display_summary(self):
        """Display a summary of the matching results."""
        if self.recommendations is None:
            print("✗ No recommendations generated yet. Run perform_matching() first.")
            return
        
        print("\n" + "="*80)
        print(" MENTOR MATCHING SYSTEM - SUMMARY REPORT")
        print("="*80)
        
        print(f"\n📊 OVERALL STATISTICS:")
        print(f"   Total Students Processed: {len(self.recommendations)}")
        print(f"   Students Matched with Mentors: {len(self.recommendations[self.recommendations['mentor_id'] != 'NONE'])}")
        print(f"   High-Risk Alerts Generated: {len(self.high_risk_alerts)}")
        
        print(f"\n🎯 URGENCY BREAKDOWN:")
        urgency_counts = self.recommendations['urgency_level'].value_counts()
        for urgency, count in urgency_counts.items():
            print(f"   {urgency}: {count} students")
        
        print(f"\n👥 PRIMARY NEEDS BREAKDOWN:")
        needs_counts = self.recommendations['primary_need'].value_counts()
        for need, count in needs_counts.items():
            print(f"   {need.capitalize()}: {count} students")
        
        print(f"\n🏆 MENTOR TYPE ASSIGNMENTS:")
        mentor_type_counts = self.recommendations['mentor_type'].value_counts()
        for mtype, count in mentor_type_counts.items():
            if mtype != 'N/A':
                print(f"   {mtype}: {count} students")
        
        print(f"\n📋 CLUSTER DISTRIBUTION:")
        cluster_counts = self.recommendations['cluster'].value_counts()
        for cluster, count in cluster_counts.items():
            print(f"   {cluster}: {count} students")
        
        if self.high_risk_alerts:
            print(f"\n🚨 HIGH-RISK ALERTS:")
            for i, alert in enumerate(self.high_risk_alerts[:5], 1):
                print(f"\n   Alert #{i}:")
                print(f"   Student: {alert['student_name']} ({alert['student_id']})")
                print(f"   Urgency: {alert['urgency']} | GPA: {alert['gpa']} | Attendance: {alert['attendance']}%")
                print(f"   Mentor: {alert['assigned_mentor']}")
                print(f"   Immediate Actions: {', '.join(alert['immediate_actions'])}")
            
            if len(self.high_risk_alerts) > 5:
                print(f"\n   ... and {len(self.high_risk_alerts) - 5} more alerts")
        
        print("\n" + "="*80)


def main():
    """Main execution function."""
    print("🎓 MENTOR MATCHING & INTERVENTION RECOMMENDATION SYSTEM")
    print("="*80)
    
    # Initialize the system
    print("\n📂 Loading data...")
    system = MentorMatchingSystem('students.csv', 'mentors.csv')
    print(f"   ✓ Loaded {len(system.students)} students")
    print(f"   ✓ Loaded {len(system.mentors)} mentors")
    
    # Perform matching
    print("\n🔄 Performing mentor-student matching...")
    recommendations = system.perform_matching()
    print(f"   ✓ Generated {len(recommendations)} recommendations")
    
    # Display summary
    system.display_summary()
    
    # Save results
    print("\n💾 Saving results...")
    system.save_recommendations('recommendations.csv')
    system.save_alerts('high_risk_alerts.csv')
    
    # Display sample recommendations
    print("\n📋 SAMPLE RECOMMENDATIONS (First 5 Students):")
    print("="*80)
    sample = recommendations.head(5)
    for idx, row in sample.iterrows():
        print(f"\n🎓 {row['student_name']} ({row['student_id']})")
        print(f"   Cluster: {row['cluster']} | GPA: {row['gpa']}")
        print(f"   Scores - Academic: {row['academic_score']}, Wellness: {row['wellness_score']}, Career: {row['career_readiness']}")
        print(f"   Primary Need: {row['primary_need'].upper()} (Urgency: {row['urgency_level']})")
        print(f"   👤 Assigned Mentor: {row['mentor_name']} ({row['mentor_type']})")
        print(f"   📅 Meeting Frequency: {row['meeting_frequency']}")
        print(f"   ⏱️  Program Duration: {row['program_duration']}")
        print(f"   📝 Key Actions:")
        print(f"      1. {row['action_1']}")
        print(f"      2. {row['action_2']}")
    
    print("\n" + "="*80)
    print("✅ MENTOR MATCHING COMPLETE!")
    print("="*80)


if __name__ == "__main__":
    main()
