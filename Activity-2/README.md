# 🎓 Student Scoring System – Rule-Based Intelligence

## Activity 2: Intelligent Student Performance Evaluation

This project transforms raw student behavioral and academic data into meaningful performance indicators using a rule-based scoring system. The goal is to help mentors quickly identify student strengths, risks, and intervention priorities through interpretable scores and readiness categories.

---

## 📌 Objective

Build an intelligent scoring framework that converts raw student data into actionable mentoring insights.

The system computes:

- Academic Performance Score (APS)
- Wellness & Wellbeing Score (WWS)
- Productivity & Time Management Score (PTMS)
- Career Readiness Score (CRS)
- Student Readiness Index (SRI)

Students are then classified into:

- 🟢 Green
- 🔵 Blue
- 🟡 Yellow
- 🔴 Red

These categories help mentors prioritize guidance and support.

---

## 📂 Deliverables

### 1. Student Dataset with Scores
**`students_scored.csv`**
Contains original student data, computed scoring metrics, and final readiness category.

### 2. Python Notebook / Script
**`student_scoring.ipynb`**
Implements rule-based scoring logic, score calculations, and the student classification system.

### 3. Scoring Logic Documentation
**`scoring_logic.pdf`**
Contains formula explanations, weight distributions, category thresholds, and interpretation logic.

---

## 🧠 Scoring System Overview

| Score | Purpose |
|---|---|
| APS | Measures academic consistency |
| WWS | Measures mental wellness and health balance |
| PTMS | Measures productivity and time management |
| CRS | Measures career preparedness and direction |
| SRI | Overall student readiness score |

---

## 📊 Scoring Logic

### 1️⃣ Academic Performance Score (APS)

Evaluates academic discipline and consistency.

| Component | Weight |
|---|---|
| GPA | 50% |
| Attendance | 25% |
| Assignment Completion | 25% |

---

### 2️⃣ Wellness & Wellbeing Score (WWS)

Evaluates psychological and physical wellbeing.

| Component | Weight |
|---|---|
| Mental Wellbeing | 40% |
| Sleep Score | 30% |
| Stress Level (inverted) | 30% |

**Sleep Score Formula** — Optimal sleep is considered ~7 hours:

```
Sleep Score = 100 - |sleep_hours - 7| × 20
```

---

### 3️⃣ Productivity & Time Management Score (PTMS)

Measures work discipline and focus.

| Component | Weight |
|---|---|
| Productivity Score | 35% |
| Distractions (inverted) | 25% |
| Engagement Score | 40% |

---

### 4️⃣ Career Readiness Score (CRS)

Evaluates preparedness for future careers.

| Component | Weight |
|---|---|
| Career Clarity | 35% |
| Skill Readiness | 35% |
| Engagement Score | 30% |

---

## 🎯 Student Readiness Index (SRI)

SRI is the final overall readiness indicator combining all four dimensions.

**Formula:**

```
SRI = 0.35(APS) + 0.20(WWS) + 0.25(PTMS) + 0.20(CRS)
```

**Weight Distribution:**

| Dimension | Weight |
|---|---|
| APS | 35% |
| PTMS | 25% |
| WWS | 20% |
| CRS | 20% |

This weighting prioritizes academics while still considering wellness, productivity, and career preparedness.

---

## 🚦 Student Classification System

| Category | SRI Range | Meaning |
|---|---|---|
| 🟢 Green | SRI ≥ 85 | Excellent overall readiness |
| 🔵 Blue | 75 ≤ SRI < 85 | Good performance with minor improvement areas |
| 🟡 Yellow | 60 ≤ SRI < 75 | Moderate risk requiring mentoring support |
| 🔴 Red | SRI < 60 | High-risk students needing immediate attention |

---

## 🔍 Behavioral Insights Captured

### 🔴 High Stress + Low Productivity
Students with high stress and low sleep often show poor productivity, reduced wellbeing, and lower SRI — typically falling into **Yellow** or **Red** categories.

### 🟡 Low GPA + High Engagement
Students who perform poorly academically but remain highly engaged indicate motivation to improve and active mentoring participation — signaling growth potential.

### 🔵 Strong Academics + Weak Career Clarity
Students with excellent GPA and productivity who lack career direction — highlighting the need for career mentorship even for academically successful students.

---

## ⚙️ Implementation Details

```
Python · Pandas · NumPy · Jupyter Notebook
```

---

## 🧪 Why Rule-Based Intelligence?

Rule-based systems were chosen because they are transparent, interpretable, and mentor-friendly. Unlike black-box ML models, mentors can clearly understand:

- Why a student received a specific score
- Which factors influenced their performance
- What interventions are needed

---

## 📈 Potential Future Enhancements

- Machine Learning prediction models
- AI mentor recommendation engines
- Student risk forecasting
- Personalized intervention systems
- Behavioral trend analytics
- Real-time mentoring dashboards

---

## 📌 Conclusion

This project successfully converts raw student data into actionable mentoring intelligence using a structured rule-based scoring framework.

The scoring system enables:

- Quick student assessment
- Risk identification
- Personalized mentoring
- Readiness evaluation
- Data-driven academic support

By combining academic, wellness, productivity, and career metrics, the system provides a holistic view of student development and readiness.
