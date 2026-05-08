# Machine Learning – Student Segmentation & Risk Detection

## Activity 3: Clustering-Based Student Intelligence System

This project focuses on applying Machine Learning techniques to identify hidden behavioral and academic patterns among students. Using clustering algorithms, students were segmented into meaningful groups such as at-risk students, high performers, and career-confused students.

The objective of this activity is to move beyond rule-based evaluation and use unsupervised learning to discover natural student groupings that can support intelligent mentoring systems.

---

# 📌 Objective

The main goal of this activity is to use Machine Learning for:

* Student segmentation
* Risk detection
* Pattern discovery
* Behavioral analysis
* Mentoring intelligence

The project applies clustering techniques to analyze relationships between:

* Academics
* Wellness
* Productivity
* Career readiness
* Student engagement

---

# 📂 Deliverables

## Files Included

### 1. Machine Learning Notebook

* `Activity_3_ML.ipynb`

Contains:

* Data preprocessing
* Feature normalization
* K-Means clustering
* Cluster analysis
* Data visualization
* ML vs Rule-Based comparison

---

### 2. Cluster Interpretation Document

* `Cluster_Interpretation.pdf` 

Contains:

* Cluster statistics
* Cluster labels
* Average metrics
* SRI comparison
* Behavioral interpretations

---

### 3. Cluster Recommendation Document

* `Cluster_Recommendations.pdf` 

Contains:

* Personalized mentoring recommendations
* Intervention strategies
* Academic and wellness support suggestions

---

# 🧠 Machine Learning Workflow

The complete ML pipeline consists of:

| Step | Description           |
| ---- | --------------------- |
| 1    | Data preprocessing    |
| 2    | Feature normalization |
| 3    | K-Means clustering    |
| 4    | Cluster analysis      |
| 5    | Visualization         |
| 6    | Comparison with SRI   |

---

# ⚙️ Data Preprocessing

Before clustering, the student dataset was cleaned and standardized.

## Preprocessing Steps

* Removed unnecessary identifiers
* Selected numerical behavioral features
* Normalized data using scaling techniques
* Ensured equal feature importance during clustering

Normalization is important because:

* GPA, attendance, stress, and engagement have different scales
* K-Means relies heavily on distance calculations

Without normalization:

* Large-scale features dominate clustering

---

# 🤖 K-Means Clustering

K-Means clustering was used to segment students into groups based on similarities in:

* Academic performance
* Stress levels
* Wellness
* Productivity
* Career readiness
* Engagement

The model identified three major student groups:

1. 🔴 At-risk Students
2. 🟡 Career-confused Students
3. 🟢 High Performers

---

# 📊 Cluster Distribution

| Cluster Type    | Number of Students |
| --------------- | ------------------ |
| Career-confused | 22                 |
| High performer  | 17                 |
| At-risk         | 11                 |

---

# 🔍 Cluster Analysis

# 🔴 Cluster 1 – At-Risk Students

Students in this cluster exhibit:

* Low GPA
* High stress
* Poor mental wellbeing
* Low career clarity
* Weak productivity

## Average Metrics

| Metric           | Average |
| ---------------- | ------- |
| GPA              | 6.30    |
| Attendance       | 76.18   |
| Stress Level     | 8.09    |
| Mental Wellbeing | 3.91    |
| Career Clarity   | 2.91    |
| SRI              | 51.35   |

---

## Characteristics

These students are:

* Academically vulnerable
* Mentally stressed
* Lacking direction
* At high mentoring risk

Most students in this cluster belong to:

* Red SRI category

---

## Recommendations

* Weekly mentoring check-ins
* Counseling support
* Time management guidance
* Academic tutoring
* Stress management workshops

---

# 🟡 Cluster 2 – Career-Confused Students

Students in this cluster show:

* Moderate-to-good academics
* Good attendance
* Strong engagement
* Unclear career goals

## Average Metrics

| Metric          | Average |
| --------------- | ------- |
| GPA             | 7.51    |
| Attendance      | 86.32   |
| Career Clarity  | 4.86    |
| Skill Readiness | 5.77    |
| SRI             | 70.90   |

---

## Characteristics

These students:

* Are motivated
* Participate actively
* Perform reasonably well academically

but:

* Lack confidence about future career paths
* Need industry exposure and mentorship

Most students fall into:

* Yellow
* Moderate SRI categories

---

## Recommendations

* Career counseling sessions
* Skill-building workshops
* Portfolio reviews
* Alumni mentorship
* Industry networking opportunities

---

# 🟢 Cluster 3 – High Performers

Students in this cluster demonstrate:

* Excellent academics
* Strong productivity
* Better mental wellbeing
* Higher skill readiness

## Average Metrics

| Metric           | Average |
| ---------------- | ------- |
| GPA              | 8.81    |
| Attendance       | 93.06   |
| Mental Wellbeing | 8.24    |
| Skill Readiness  | 7.41    |
| SRI              | 81.32   |

---

## Characteristics

These students:

* Maintain strong academic discipline
* Show consistent engagement
* Possess better career readiness

Most students belong to:

* Blue
* Green categories

---

## Recommendations

* Advanced projects
* Leadership opportunities
* Research programs
* Internship guidance
* Peer mentoring roles

---

# 📈 ML Insights vs Rule-Based SRI

One major objective was comparing:

* Rule-based scoring system (SRI)
  vs
* Machine Learning clustering

---

# 🔍 Observations

## Strong Alignment

High performers identified by K-Means also:

* Had high SRI scores
* Belonged mostly to Blue/Green categories

---

## Additional ML Insights

Machine Learning revealed:

* Hidden behavioral similarities
* Students with moderate SRI but unclear career direction
* Risk groups not obvious through scoring alone

---

## Why ML Adds Value

Unlike fixed rule systems:

* Clustering adapts to hidden patterns
* Finds natural student groups
* Identifies nuanced mentoring needs

This makes ML more powerful for:

* Personalized mentoring
* Risk prediction
* Intelligent intervention systems

---

# 📊 Visualization & Insights

The notebook includes visualizations such as:

* Cluster scatter plots
* PCA-based 2D cluster projections
* Feature distribution graphs
* SRI vs Cluster comparisons

These visuals help:

* Understand student grouping behavior
* Interpret cluster separations
* Validate ML model quality

---

# 🧪 Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Core implementation  |
| Pandas       | Data handling        |
| NumPy        | Numerical operations |
| Scikit-learn | K-Means clustering   |
| Matplotlib   | Visualization        |
| Seaborn      | Statistical plotting |

---

# 🚀 Future Improvements

The project can be extended using:

* Hierarchical clustering
* DBSCAN clustering
* Predictive ML models
* Early warning systems
* AI-powered mentoring assistants
* Real-time student analytics dashboards

---

# 📌 Conclusion

This project successfully demonstrates how Machine Learning can be used to uncover hidden student behavioral patterns and mentoring risk groups.

By combining:

* Academic metrics
* Wellness indicators
* Productivity patterns
* Career readiness

the clustering system provides deeper insights than traditional scoring methods alone.

The ML-driven segmentation framework enables:

* Personalized mentoring
* Early risk detection
* Smarter interventions
* Better student development strategies

This forms a strong foundation for building intelligent AI-powered student mentoring platforms.
