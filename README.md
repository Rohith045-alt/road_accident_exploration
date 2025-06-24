# Road Accident Survival Analysis (India)

This project explores a synthetic dataset of 100 road accident victims across Indian states to identify key patterns influencing survival outcomes. The analysis is performed using Python (Pandas, Seaborn, Matplotlib) and follows a structured EDA (Exploratory Data Analysis) process.

---

## Dataset Description

Each row represents an accident victim, with features including:

- `Age` — Age of the person
- `Survived` — Whether the person survived (Yes/No)
- `InjuryType` — Major or Minor injury
- `BloodRequired` — If emergency blood was needed
- `Abandoned` — If the person was left without assistance
- Additional fields: Name, City, State, Passenger ID, etc.

---

## Objective

To identify patterns, trends, and anomalies affecting survival, and make basic feature-level inferences.

---

## Key Visual Insights

1. **Age vs Survival**
   - Younger age groups show higher survival rates.
   - Elderly (60+) are at greater risk, showing a negative correlation with survival.

2. **Injury Type vs Survival**
   - **Major injuries** significantly reduce survival likelihood.
   - Strong negative relationship between severity and outcome.

3. **Blood Requirement**
   - Needing emergency blood correlates with lower survival.
   - Indicates high trauma level in those cases.

4. **Abandonment**
   - Victims who were **abandoned** after the accident had lower survival rates.
   - Highlights importance of immediate medical response.

5. **Anomalies**
   - A few individuals with **minor injuries** did not survive.
   - These are considered outliers or special cases, possibly due to comorbidities or delayed care.

---

## Feature-Level Inferences

| Feature         | Influence on Survival                  |
|------------------|-----------------------------------------|
| `Age`            | Moderate negative impact               |
| `InjuryType`     | Strong negative impact                 |
| `BloodRequired`  | Strong negative impact                 |
| `Abandoned`      | Moderate negative impact               |
| `Minor Deaths`   | Possible anomalies, needs investigation|

---

## Conclusion

This dataset demonstrates how survival in road accidents is significantly influenced by injury severity, age, medical attention, and emergency response. These findings can help inform healthcare prioritization and policy design.
