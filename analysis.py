#STEP 1: Generate summary statistics 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('road_accident.csv')
df['Survived'] = df['Survived'].str.strip().str.capitalize()
df['BloodRequired'] = df['BloodRequired'].map({'Yes': 1, 'No': 0})
df['Abandoned'] = df['Abandoned'].map({'Yes': 1, 'No': 0})
df['Survived'] = df['Survived'].map({'Yes': 1, 'No': 0})
df['InjuryType'] = df['InjuryType'].str.strip().map({'Major': 1, 'Minor': 0})
df.describe()

#STEP 2: Create histograms and boxplots for numeric features

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df = pd.read_csv("road_accident.csv")
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Survived'] = df['Survived'].str.strip().str.capitalize()  
#1. Age Histogram and Boxplot
fig, axs = plt.subplots(1, 2, figsize=(14, 5)
sns.histplot(df['Age'], bins=10, kde=True, ax=axs[0], color='skyblue')
axs[0].set_title('Age Distribution - Histogram')
axs[0].set_xlabel('Age')

sns.boxplot(x=df['Age'], ax=axs[1], color='lightgreen')
axs[1].set_title('Age Distribution - Boxplot')

plt.tight_layout()
plt.show()
#2. Survived Count Plot
plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df, palette='pastel')
plt.title('Survival Count')
plt.xlabel('Survived')
plt.ylabel('Number of Passengers')
plt.show()

# 3. Age Distribution Split by Survived
plt.figure(figsize=(8,5))
sns.histplot(data=df, x='Age', hue='Survived', bins=10, kde=True, palette='Set2', multiple='stack')
plt.title('Age Distribution by Survival Status')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

#STEP 3: Use pairplot/correlation matrix for feature relationships

#Shows the rate of survival with major and minor injuries
df['Survived'] = df['Survived'].str.strip().map({'Yes': 1, 'No': 0})
df['InjuryType'] = df['InjuryType'].str.strip().map({'Major': 1, 'Minor': 0})
injury_survival = df.groupby('InjuryType')['Survived'].mean().reset_index()
injury_survival['InjuryType'] = injury_survival['InjuryType'].map({1: 'Minor', 0: 'Major'})
print(injury_survival)

#Visualize the rate of survival  
sns.barplot(x='InjuryType', y='Survived', data=injury_survival, palette='Set1')
plt.title('Survival Rate by Injury Type')
plt.ylabel('Survival Rate')
plt.xlabel('Injury Type')
plt.ylim(0, 1)
plt.show()

#STEP 4: Identify patterns, trends, or anomalies in the data

#Shows the anomaly in the rate of survival with major and minor injuries
df['InjuryType'] = df['InjuryType'].str.strip().map({'Major': 0, 'Minor': 1})
df['Survived'] = df['Survived'].str.strip().map({'Yes': 1, 'No': 0})
df['Group'] = df.apply(lambda x: f"{'Major' if x['InjuryType'] == 1 else 'Minor'} Injury - {'Survived' if x['Survived'] == 1 else 'Died'}", axis=1)
group_counts = df['Group'].value_counts().reset_index()
group_counts.columns = ['Case', 'Count']
plt.figure(figsize=(8,5))
sns.barplot(x='Case', y='Count', data=group_counts, palette='coolwarm')
plt.title('Survival vs Injury Type (Including Anomalies)')
plt.ylabel('Number of People')
plt.xlabel('Case Type')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

#Shows pattern (Blood Required = Higher Risk)

df['BloodRequired'] = df['BloodRequired'].str.strip().map({'Yes': 1, 'No': 0})
df.groupby('BloodRequired')['Survived'].mean()
