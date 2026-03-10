# Activity 4: Mentor Matching & Intervention Recommendations

## 📚 Overview

This project implements an intelligent mentor-student matching system that translates student performance insights into actionable mentoring interventions. The system analyzes student needs across academic, wellness, and career dimensions to provide personalized mentor assignments and intervention strategies.

---

## 🎯 Objectives Completed

✅ **Designed comprehensive mentor dataset** (`mentors.csv`)  
✅ **Created student dataset with clusters** (`students.csv`)  
✅ **Implemented intelligent matching logic** (`mentor_matching.py`)  
✅ **Generated recommendation tables** (`recommendations.csv`)  
✅ **Simulated high-risk alerts** (`high_risk_alerts.csv`)  
✅ **Documented end-to-end process flow**

---

## 📊 Data Components

### 1. Student Dataset (`students.csv`)
**30 students** with the following attributes:
- **Academic Metrics**: academic_score, gpa, assignment_completion
- **Wellness Indicators**: wellness_score, stress_level
- **Career Readiness**: career_readiness score
- **Behavioral Data**: attendance percentage
- **Cluster Assignment**: High_Performer, Balanced, Struggling, At_Risk

### 2. Mentor Dataset (`mentors.csv`)
**20 mentors** across three categories:
- **Academic Mentors** (8): Subject matter experts in various disciplines
- **Wellness Mentors** (6): Mental health, stress management, and well-being specialists
- **Career Mentors** (6): Industry professionals, career counselors, and networking experts

Each mentor has:
- Specialization area
- Availability level (High/Medium/Low)
- Maximum student capacity
- Years of experience
- Contact information

---

## 🔄 End-to-End Process Flow

### **Step 1: Student Needs Analysis**

For each student, the system calculates need scores across three dimensions:

```
Need Score = 100 - Performance Score
```

- **Academic Need** = 100 - academic_score
- **Wellness Need** = 100 - wellness_score  
- **Career Need** = 100 - career_readiness

The dimension with the **highest need score** becomes the **primary need**.

**Example:**
- Student: Alice Johnson
- Academic Score: 85 → Need: 15
- Wellness Score: 70 → Need: 30
- Career Score: 65 → Need: **35** ✓ (Primary Need)
- **Result**: Alice needs career mentoring most

---

### **Step 2: Urgency Assessment**

The system evaluates five risk factors to determine intervention urgency:

| Risk Factor | Condition |
|------------|-----------|
| Low GPA | GPA < 2.0 |
| Low Attendance | Attendance < 60% |
| Low Completion | Assignment Completion < 60% |
| High Stress | Stress Level = High or Very High |
| At-Risk Cluster | Cluster = "At_Risk" |

**Urgency Levels:**
- **Critical** (4-5 risk factors): Immediate daily/3x weekly intervention
- **High** (3 risk factors): 2x weekly intervention
- **Medium** (2 risk factors): Weekly intervention
- **Low** (0-1 risk factors): Bi-weekly or monthly check-ins

**Example:**
- Student: David Lee
- GPA: 1.9 ✓
- Attendance: 55% ✓
- Completion: 50% ✓
- Stress: Very High ✓
- Cluster: At_Risk ✓
- **Risk Score: 5/5** → **CRITICAL URGENCY**

---

### **Step 3: Mentor Matching Algorithm**

The matching algorithm follows these steps:

1. **Filter by Mentor Type**: Match primary need to mentor expertise
   - Academic Need → Academic Mentors
   - Wellness Need → Wellness Mentors
   - Career Need → Career Mentors

2. **Calculate Match Score** based on:
   - **Availability**: High (3 pts), Medium (2 pts), Low (1 pt)
   - **Specialization Match**: +2 pts if mentor's expertise aligns with student's major
   - **Experience Bonus**: For Critical/High urgency cases, add experience_years/5

3. **Select Best Match**: Mentor with highest match score

4. **Capacity Management**: Track mentor-student ratios (future enhancement)

**Example Matching:**
- Student: Leo Garcia (Computer Science major, Critical urgency)
- Primary Need: Career
- Available Career Mentors: 6
- Best Match: Dr. Michael Brown (Career, Medium availability, 20 years experience)
- Match Score: 2 (availability) + 0 (specialization) + 4 (experience) = **6 points**

---

### **Step 4: Intervention Generation**

Based on **primary need** and **urgency level**, the system prescribes:

#### **Academic Interventions**
- **Critical**: 1-on-1 tutoring 3x/week, probation support, course load reduction
- **High**: Tutoring 2x/week, study groups, assignment planning
- **Medium**: Bi-weekly tutoring, study techniques workshop
- **Low**: Monthly check-ins, resource recommendations

#### **Wellness Interventions**
- **Critical**: Immediate counseling, daily check-ins, stress management intensive
- **High**: Weekly counseling, stress reduction workshop, peer support
- **Medium**: Bi-weekly wellness check-ins, mindfulness workshop
- **Low**: Monthly check-ins, self-care resources

#### **Career Interventions**
- **Critical**: Intensive weekly counseling, internship search, resume overhaul, interview bootcamp
- **High**: Bi-weekly career planning, networking events, job search strategy
- **Medium**: Monthly guidance, resume review, career fair
- **Low**: Semester planning, industry exploration, alumni networking

---

### **Step 5: High-Risk Alert System**

For students with **Critical** or **High** urgency, the system generates automated alerts containing:

- Timestamp of alert generation
- Student identification and contact information
- Risk indicators (GPA, attendance, stress level)
- Assigned mentor details
- Immediate action items (top 2 priorities)
- Alert classification (CRITICAL or HIGH_PRIORITY)

**Alert Recipients** (in production):
- Academic advisors
- Department heads
- Student counseling services
- Assigned mentor
- Student success team

---

## 📈 System Results

### Overall Statistics
- **Total Students Processed**: 30
- **Successfully Matched**: 30 (100%)
- **High-Risk Alerts**: 7 students (23%)

### Urgency Distribution
- **Critical**: 4 students (13%)
- **High**: 3 students (10%)
- **Medium**: 1 student (3%)
- **Low**: 22 students (73%)

### Primary Needs Breakdown
- **Career**: 18 students (60%)
- **Wellness**: 7 students (23%)
- **Academic**: 5 students (17%)

### Cluster Analysis
- **High Performers**: 8 students → Mostly Low urgency, career-focused
- **Balanced**: 8 students → Mixed needs, generally Low urgency
- **Struggling**: 6 students → Medium urgency, academic/wellness needs
- **At-Risk**: 8 students → High/Critical urgency, comprehensive support needed

---

## 🎓 Key Insights

### 1. **Career Readiness Gap**
60% of students identified career development as their primary need, indicating a significant gap in professional preparation across all performance levels.

**Recommendation**: Increase career mentoring resources and integrate career development into curriculum.

### 2. **At-Risk Student Profile**
All 4 Critical urgency students belong to the At-Risk cluster with:
- GPA < 2.0
- Attendance < 65%
- Very High stress levels
- Multiple concurrent deficits

**Recommendation**: Early warning system should trigger proactive interventions before students reach critical status.

### 3. **Wellness Support Demand**
23% of students need primary wellness support, with strong correlation to academic performance.

**Recommendation**: Mental health resources should be scaled, particularly stress management programs.

### 4. **Mentor Allocation**
- Career mentors are most in-demand (18 students)
- Current mentor capacity appears adequate
- Dr. Michael Brown (Career) matched with 4 high-urgency students due to high experience

**Recommendation**: Recruit additional experienced career mentors to distribute high-urgency cases.

---

## 🚀 Implementation Guide

### Running the System

1. **Ensure Data Files** are in the working directory:
   - `students.csv`
   - `mentors.csv`

2. **Execute Matching Script**:
   ```bash
   python3 mentor_matching.py
   ```

3. **Review Outputs**:
   - `recommendations.csv` - Complete matching results for all students
   - `high_risk_alerts.csv` - Critical alerts requiring immediate action

### Customization Options

#### Adjust Risk Thresholds
In `mentor_matching.py`, modify the `_calculate_urgency()` method:
```python
risk_factors = {
    'low_gpa': 1 if student['gpa'] < 2.0 else 0,  # Change threshold
    'low_attendance': 1 if student['attendance'] < 60 else 0,
    # ... adjust other thresholds
}
```

#### Modify Intervention Strategies
Update the `interventions` dictionary in `generate_intervention()` method to customize action plans.

#### Change Meeting Frequencies
Adjust the `_get_meeting_frequency()` and `_get_program_duration()` methods.

---

## 📋 Output Files

### 1. `recommendations.csv`
**Columns:**
- Student identification (ID, name, cluster)
- Performance scores (academic, wellness, career, GPA)
- Need analysis (primary_need, urgency_level)
- Mentor assignment (mentor_id, name, type, expertise)
- Intervention plan (type, frequency, duration)
- Specific actions (action_1, action_2, action_3)

**Use Cases:**
- Student success team reviews and implements recommendations
- Academic advisors track intervention progress
- Department heads monitor at-risk student support
- Data analysts evaluate program effectiveness

### 2. `high_risk_alerts.csv`
**Columns:**
- Alert metadata (timestamp, alert_type)
- Student information (ID, name, GPA, attendance, stress_level)
- Urgency indicators
- Mentor assignment (name, contact)
- Immediate actions required

**Use Cases:**
- Trigger emergency intervention protocols
- Notify relevant stakeholders immediately
- Track critical student outcomes
- Measure response time and effectiveness

---

## 🔬 Methodology Strengths

1. **Data-Driven**: Decisions based on quantified student metrics
2. **Holistic**: Considers academic, wellness, and career dimensions
3. **Prioritized**: Urgency-based resource allocation
4. **Scalable**: Automated matching handles large student populations
5. **Transparent**: Clear logic for matching and intervention decisions
6. **Actionable**: Specific, time-bound action plans for each student

---

## 🎯 Future Enhancements

### 1. **Machine Learning Integration**
- Train predictive models on historical intervention outcomes
- Learn optimal mentor-student pairings from success data
- Predict student risk trajectory before crisis points

### 2. **Dynamic Capacity Management**
- Track real-time mentor workload
- Prevent overallocation to individual mentors
- Balance caseloads across mentor pool

### 3. **Outcome Tracking**
- Measure intervention effectiveness
- Track GPA improvement, stress reduction, career placements
- Generate effectiveness reports per mentor and intervention type

### 4. **Student Preferences**
- Incorporate student input on mentor preferences
- Consider cultural, language, and identity factors
- Enable student-initiated mentor requests

### 5. **Feedback Loop**
- Collect student and mentor satisfaction scores
- Adjust matching algorithm based on feedback
- Continuous improvement of intervention strategies

### 6. **Integration with Campus Systems**
- Sync with LMS for real-time academic data
- Connect to counseling appointment systems
- Interface with career services platforms

---

## 📚 Technical Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   INPUT DATA LAYER                      │
├─────────────────────────────────────────────────────────┤
│  students.csv                    mentors.csv            │
│  - Performance Metrics           - Expertise Areas      │
│  - Cluster Assignments           - Availability         │
│  - Behavioral Indicators         - Capacity             │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│              ANALYSIS & MATCHING ENGINE                 │
├─────────────────────────────────────────────────────────┤
│  1. Student Needs Analysis                              │
│     └─ Calculate need scores for academic/wellness/career│
│                                                          │
│  2. Urgency Assessment                                  │
│     └─ Evaluate risk factors & assign urgency level     │
│                                                          │
│  3. Mentor Matching Algorithm                           │
│     └─ Filter → Score → Select best match               │
│                                                          │
│  4. Intervention Generation                             │
│     └─ Prescribe actions based on need × urgency        │
│                                                          │
│  5. Alert System                                        │
│     └─ Trigger high-risk notifications                  │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                   OUTPUT DATA LAYER                     │
├─────────────────────────────────────────────────────────┤
│  recommendations.csv          high_risk_alerts.csv      │
│  - Complete matching results  - Critical notifications  │
│  - Intervention plans         - Immediate actions       │
│  - Mentor assignments         - Emergency contacts      │
└─────────────────────────────────────────────────────────┘
```

---

## 💡 Sample Use Cases

### **Use Case 1: Critical Student Intervention**
**Student**: Leo Garcia (S012)
- **Situation**: GPA 1.8, 52% attendance, Very High stress, At-Risk cluster
- **System Action**: 
  - Urgency: CRITICAL
  - Matched with: Dr. Michael Brown (Career Mentor, 20 years experience)
  - Intervention: Intensive career counseling weekly, immediate internship search support, resume overhaul, interview bootcamp
  - Alert Generated: Yes (CRITICAL priority)
  - Meeting Frequency: Daily/3x per week
  - Duration: 1 semester with intensive support

### **Use Case 2: Balanced Student Career Support**
**Student**: Carol White (S003)
- **Situation**: GPA 3.2, adequate wellness, needs career development
- **System Action**:
  - Urgency: LOW
  - Matched with: Mr. David Kumar (Career Mentor, Resume & Interview Prep)
  - Intervention: Semester career planning, industry exploration, alumni networking
  - Alert Generated: No
  - Meeting Frequency: Bi-weekly or Monthly
  - Duration: 4-6 weeks

### **Use Case 3: High Performer Wellness Check**
**Student**: Emma Brown (S005)
- **Situation**: Excellent academic performance, moderate wellness concern
- **System Action**:
  - Urgency: LOW
  - Matched with: Ms. Lisa Thompson (Wellness Mentor, Mental Health)
  - Intervention: Monthly wellness check-ins, self-care resources, campus wellness activities
  - Alert Generated: No
  - Meeting Frequency: Bi-weekly or Monthly
  - Duration: 4-6 weeks

---

## ✅ Deliverables Summary

| # | Deliverable | File | Status |
|---|------------|------|--------|
| 1 | Mentor Dataset | `mentors.csv` | ✅ Complete |
| 2 | Student Dataset | `students.csv` | ✅ Complete |
| 3 | Matching Logic | `mentor_matching.py` | ✅ Complete |
| 4 | Recommendations Table | `recommendations.csv` | ✅ Generated |
| 5 | High-Risk Alerts | `high_risk_alerts.csv` | ✅ Generated |
| 6 | Documentation | `README.md` | ✅ Complete |

---

## 🎓 Conclusion

This mentor matching system successfully transforms student performance data into actionable mentoring interventions. By combining quantitative analysis with expert mentor assignments and structured intervention plans, the system provides a scalable framework for student support services.

**Key Achievements:**
- 100% student coverage with personalized mentor matches
- Automated risk detection and alert generation
- Evidence-based intervention recommendations
- Transparent, reproducible matching methodology

**Impact Potential:**
- Early identification and support for struggling students
- Efficient allocation of mentoring resources
- Data-driven student success strategies
- Improved retention and graduation outcomes

---

**Project Status**: ✅ **COMPLETE**  
**Author**: Student Mentoring System Development Team  
**Date**: February 2026  
**Version**: 1.0
