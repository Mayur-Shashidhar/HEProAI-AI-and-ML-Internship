"""
Visualization and Analysis Script for Mentor Matching System
Generates charts and detailed analytics for the recommendation results
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

def load_data():
    """Load recommendations and alerts data."""
    try:
        recommendations = pd.read_csv('recommendations.csv')
        alerts = pd.read_csv('high_risk_alerts.csv')
        return recommendations, alerts
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please run mentor_matching.py first to generate the data files.")
        return None, None

def create_urgency_distribution(recommendations):
    """Create urgency level distribution chart."""
    plt.figure(figsize=(10, 6))
    urgency_counts = recommendations['urgency_level'].value_counts()
    colors = {'Critical': '#d32f2f', 'High': '#f57c00', 'Medium': '#fbc02d', 'Low': '#388e3c'}
    
    urgency_order = ['Critical', 'High', 'Medium', 'Low']
    urgency_data = [urgency_counts.get(level, 0) for level in urgency_order]
    urgency_colors = [colors[level] for level in urgency_order]
    
    bars = plt.bar(urgency_order, urgency_data, color=urgency_colors, alpha=0.7, edgecolor='black')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.title('Student Distribution by Urgency Level', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Urgency Level', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Students', fontsize=12, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('urgency_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: urgency_distribution.png")
    plt.close()

def create_needs_distribution(recommendations):
    """Create primary needs distribution pie chart."""
    plt.figure(figsize=(10, 8))
    needs_counts = recommendations['primary_need'].value_counts()
    
    colors = ['#2196f3', '#4caf50', '#ff9800']
    explode = (0.05, 0.05, 0.05)
    
    plt.pie(needs_counts.values, labels=[n.capitalize() for n in needs_counts.index],
            autopct='%1.1f%%', startangle=90, colors=colors, explode=explode,
            textprops={'fontsize': 12, 'fontweight': 'bold'})
    
    plt.title('Primary Student Needs Distribution', fontsize=16, fontweight='bold', pad=20)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('needs_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: needs_distribution.png")
    plt.close()

def create_cluster_urgency_heatmap(recommendations):
    """Create heatmap showing urgency levels across clusters."""
    plt.figure(figsize=(10, 6))
    
    # Create cross-tabulation
    cluster_urgency = pd.crosstab(recommendations['cluster'], 
                                   recommendations['urgency_level'])
    
    # Reorder columns for better visualization
    column_order = [col for col in ['Critical', 'High', 'Medium', 'Low'] 
                   if col in cluster_urgency.columns]
    cluster_urgency = cluster_urgency[column_order]
    
    sns.heatmap(cluster_urgency, annot=True, fmt='d', cmap='YlOrRd', 
                cbar_kws={'label': 'Number of Students'}, linewidths=0.5)
    
    plt.title('Student Distribution: Cluster vs Urgency Level', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Urgency Level', fontsize=12, fontweight='bold')
    plt.ylabel('Student Cluster', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig('cluster_urgency_heatmap.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: cluster_urgency_heatmap.png")
    plt.close()

def create_mentor_type_distribution(recommendations):
    """Create mentor type assignment distribution."""
    plt.figure(figsize=(10, 6))
    
    mentor_counts = recommendations['mentor_type'].value_counts()
    # Remove 'N/A' if present
    mentor_counts = mentor_counts[mentor_counts.index != 'N/A']
    
    colors = ['#3f51b5', '#009688', '#ff5722']
    bars = plt.bar(range(len(mentor_counts)), mentor_counts.values, 
                   color=colors, alpha=0.7, edgecolor='black')
    
    plt.xticks(range(len(mentor_counts)), mentor_counts.index, fontsize=11)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.title('Student Distribution by Mentor Type', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Mentor Type', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Students Assigned', fontsize=12, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('mentor_type_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: mentor_type_distribution.png")
    plt.close()

def create_score_comparison(recommendations):
    """Create box plot comparing scores across clusters."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    
    score_types = [
        ('academic_score', 'Academic Score', '#2196f3'),
        ('wellness_score', 'Wellness Score', '#4caf50'),
        ('career_readiness', 'Career Readiness', '#ff9800')
    ]
    
    for idx, (score_col, title, color) in enumerate(score_types):
        ax = axes[idx]
        
        cluster_order = ['High_Performer', 'Balanced', 'Struggling', 'At_Risk']
        cluster_data = [recommendations[recommendations['cluster'] == cluster][score_col].values 
                       for cluster in cluster_order if cluster in recommendations['cluster'].values]
        cluster_labels = [cluster for cluster in cluster_order 
                         if cluster in recommendations['cluster'].values]
        
        bp = ax.boxplot(cluster_data, labels=cluster_labels, patch_artist=True,
                       medianprops={'color': 'red', 'linewidth': 2},
                       boxprops={'facecolor': color, 'alpha': 0.6})
        
        ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
        ax.set_xlabel('Student Cluster', fontsize=11, fontweight='bold')
        ax.set_ylabel('Score', fontsize=11, fontweight='bold')
        ax.tick_params(axis='x', rotation=15)
        ax.grid(axis='y', alpha=0.3)
    
    plt.suptitle('Performance Scores by Student Cluster', 
                fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('score_comparison_by_cluster.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: score_comparison_by_cluster.png")
    plt.close()

def create_gpa_distribution(recommendations):
    """Create GPA distribution histogram with urgency overlay."""
    plt.figure(figsize=(12, 6))
    
    urgency_colors = {'Critical': '#d32f2f', 'High': '#f57c00', 
                     'Medium': '#fbc02d', 'Low': '#388e3c'}
    
    for urgency in ['Critical', 'High', 'Medium', 'Low']:
        data = recommendations[recommendations['urgency_level'] == urgency]['gpa']
        if len(data) > 0:
            plt.hist(data, bins=15, alpha=0.6, label=urgency, 
                    color=urgency_colors[urgency], edgecolor='black')
    
    plt.axvline(x=2.0, color='red', linestyle='--', linewidth=2, label='Risk Threshold (GPA 2.0)')
    
    plt.title('GPA Distribution by Urgency Level', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('GPA', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Students', fontsize=12, fontweight='bold')
    plt.legend(loc='upper left', fontsize=10)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('gpa_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: gpa_distribution.png")
    plt.close()

def generate_detailed_statistics(recommendations, alerts):
    """Generate detailed statistical summary."""
    print("\n" + "="*80)
    print(" DETAILED STATISTICAL ANALYSIS")
    print("="*80)
    
    # Overall statistics
    print("\n📊 OVERALL METRICS:")
    print(f"   Total Students: {len(recommendations)}")
    print(f"   Average GPA: {recommendations['gpa'].mean():.2f}")
    print(f"   Median GPA: {recommendations['gpa'].median():.2f}")
    print(f"   GPA Range: {recommendations['gpa'].min():.1f} - {recommendations['gpa'].max():.1f}")
    
    # Score statistics
    print("\n📈 AVERAGE SCORES BY CLUSTER:")
    cluster_stats = recommendations.groupby('cluster')[
        ['academic_score', 'wellness_score', 'career_readiness', 'gpa']
    ].mean()
    print(cluster_stats.to_string())
    
    # Urgency by cluster
    print("\n🎯 URGENCY DISTRIBUTION BY CLUSTER:")
    urgency_cluster = pd.crosstab(recommendations['cluster'], 
                                   recommendations['urgency_level'], 
                                   margins=True)
    print(urgency_cluster.to_string())
    
    # Mentor assignments
    print("\n👥 TOP ASSIGNED MENTORS:")
    top_mentors = recommendations['mentor_name'].value_counts().head(10)
    for i, (mentor, count) in enumerate(top_mentors.items(), 1):
        print(f"   {i}. {mentor}: {count} students")
    
    # Alert analysis
    if len(alerts) > 0:
        print("\n🚨 HIGH-RISK ALERT ANALYSIS:")
        print(f"   Total Alerts: {len(alerts)}")
        alert_types = alerts['alert_type'].value_counts()
        for alert_type, count in alert_types.items():
            print(f"   {alert_type}: {count} alerts")
        print(f"   Average GPA of High-Risk Students: {alerts['gpa'].mean():.2f}")
        print(f"   Average Attendance of High-Risk Students: {alerts['attendance'].mean():.1f}%")
    
    # Meeting frequency analysis
    print("\n📅 MEETING FREQUENCY DISTRIBUTION:")
    frequency_counts = recommendations['meeting_frequency'].value_counts()
    for freq, count in frequency_counts.items():
        print(f"   {freq}: {count} students")
    
    print("\n" + "="*80)

def create_performance_scatter(recommendations):
    """Create scatter plot of academic vs wellness scores."""
    plt.figure(figsize=(12, 8))
    
    urgency_colors = {'Critical': '#d32f2f', 'High': '#f57c00', 
                     'Medium': '#fbc02d', 'Low': '#388e3c'}
    
    for urgency in recommendations['urgency_level'].unique():
        data = recommendations[recommendations['urgency_level'] == urgency]
        plt.scatter(data['academic_score'], data['wellness_score'],
                   c=urgency_colors[urgency], label=urgency, 
                   alpha=0.6, s=100, edgecolors='black', linewidth=1)
    
    plt.axhline(y=50, color='gray', linestyle='--', alpha=0.5, label='Average Line')
    plt.axvline(x=50, color='gray', linestyle='--', alpha=0.5)
    
    plt.title('Academic vs Wellness Performance by Urgency', 
             fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Academic Score', fontsize=12, fontweight='bold')
    plt.ylabel('Wellness Score', fontsize=12, fontweight='bold')
    plt.legend(title='Urgency Level', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('performance_scatter.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: performance_scatter.png")
    plt.close()

def main():
    """Main execution function."""
    print("\n" + "="*80)
    print(" MENTOR MATCHING VISUALIZATION & ANALYSIS")
    print("="*80)
    
    # Load data
    print("\n📂 Loading data...")
    recommendations, alerts = load_data()
    
    if recommendations is None:
        return
    
    print(f"   ✓ Loaded {len(recommendations)} recommendations")
    print(f"   ✓ Loaded {len(alerts)} high-risk alerts")
    
    # Generate visualizations
    print("\n📊 Generating visualizations...")
    create_urgency_distribution(recommendations)
    create_needs_distribution(recommendations)
    create_cluster_urgency_heatmap(recommendations)
    create_mentor_type_distribution(recommendations)
    create_score_comparison(recommendations)
    create_gpa_distribution(recommendations)
    create_performance_scatter(recommendations)
    
    # Generate statistics
    generate_detailed_statistics(recommendations, alerts)
    
    print("\n✅ ANALYSIS COMPLETE!")
    print("="*80)
    print("\n📁 Generated Files:")
    print("   • urgency_distribution.png")
    print("   • needs_distribution.png")
    print("   • cluster_urgency_heatmap.png")
    print("   • mentor_type_distribution.png")
    print("   • score_comparison_by_cluster.png")
    print("   • gpa_distribution.png")
    print("   • performance_scatter.png")
    print("\n" + "="*80)

if __name__ == "__main__":
    main()
