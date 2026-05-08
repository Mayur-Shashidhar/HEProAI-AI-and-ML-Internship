# 🎓 Student Mentoring Dataset – Activity 1

A synthetic dataset simulating realistic student behavior across academics, wellness, productivity, engagement, and career readiness — designed for mentoring analytics, behavioral pattern identification, and machine learning applications.

---

## 📌 Objective

Simulate real-world student behavior through structured data to surface meaningful mentoring insights, including:

- High stress leading to low productivity
- Students with low GPA but high engagement
- Strong academic performers lacking career clarity
- Wellness impacting academic consistency
- Productivity patterns based on sleep and distractions

---

## 📊 Dataset Overview

The dataset contains **50 synthetic student records**, each representing a combination of:

| Dimension | Examples |
|---|---|
| Academic Performance | GPA, attendance, assignment completion |
| Wellness Indicators | Stress level, sleep hours, mental wellbeing |
| Productivity Metrics | Productivity score, distractions |
| Career Preparedness | Career clarity, skill readiness |
| Platform Engagement | Engagement score |

---

## 🧠 Data Dictionary

| Column | Description | Range / Type |
|---|---|---|
| `student_id` | Unique student identifier | Categorical |
| `age` | Student age | 18–25 |
| `program` | Degree program | B.Tech / MBA |
| `semester` | Current semester | 1–8 |
| `gpa` | Academic performance score | 0–10 |
| `attendance` | Attendance percentage | 0–100 |
| `assignments_completion` | Assignment completion percentage | 0–100 |
| `stress_level` | Self-reported stress level | 1–10 |
| `sleep_hours` | Average sleep hours per night | 0–10 |
| `mental_wellbeing` | Psychological wellbeing score | 1–10 |
| `productivity_score` | Time management & productivity score | 1–10 |
| `distractions` | Level of distractions | 1–10 |
| `career_clarity` | Career goal clarity score | 1–10 |
| `skill_readiness` | Industry/job readiness score | 1–10 |
| `engagement_score` | Mentoring platform engagement score | 0–100 |

---

## ⚙️ Dataset Design Strategy

Data was generated to simulate realistic behavioral patterns rather than purely random values:

**Academic Performance** — Higher attendance, better assignment completion, and lower distractions correlate with higher GPA, productivity, and skill readiness.

**Stress & Wellness** — High stress combined with low sleep reduces productivity, mental wellbeing, and academic consistency.

**Engagement Variability** — Some students with low GPA show high platform engagement, reflecting motivation and a desire to improve.

**Career Clarity Gaps** — Strong academic performers may still lack career direction, creating realistic mentoring scenarios.

---

## 🔍 Behavioral Patterns

### 🔴 High Stress + Low Productivity
Students with stress > 7 and sleep < 5 hours typically show below-average productivity, lower mental wellbeing, and reduced assignment consistency — indicative of burnout.

### 🟡 Low GPA + High Engagement
Students with GPA < 6 but engagement > 75 are actively seeking improvement. These growth-oriented learners are prime candidates for targeted mentoring.

### 🟢 Strong Academics + Unclear Career Goals
Students with GPA > 8 and high attendance who still score low on career clarity — highlighting the need for career counseling alongside academic support.

---

## 🧪 Why Synthetic Data?

- Avoids privacy concerns associated with real student data
- Enables controlled creation of behavioral patterns
- Ideal for ML experimentation and safe academic research
- Supports prototyping of mentoring and analytics systems

---

## 🚀 Potential Use Cases

- Academic performance prediction
- Student clustering and segmentation
- Stress and burnout detection
- Productivity analysis
- Personalized mentor recommendation systems
- Student dropout risk prediction
- Career path recommendation engines

---

## 🛠️ Suggested Tools

```
Python · Pandas · NumPy · Scikit-learn · Matplotlib · Power BI · Tableau
```

---

## 🔭 Future Extensions

- Placement status prediction
- Personality profiling
- Emotional sentiment analysis
- AI-based mentor matching
- Student dropout risk modeling

---

## 📌 Conclusion

This project successfully models realistic student mentoring scenarios through a structured synthetic dataset. The data captures complex relationships between academic performance, wellness, productivity, engagement, and career preparedness.

The dataset is suitable for:

- Mentoring analytics
- Educational research
- AI/ML experimentation
- Student behavior analysis
- Predictive modeling systems

It provides a strong foundation for building intelligent student mentoring platforms and future educational AI systems.
