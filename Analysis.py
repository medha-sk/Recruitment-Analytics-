# Recruitment Analytics Project
# Exploratory Data Analysis (EDA)

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Data/job_applicant_dataset.csv")

print("=" * 50)
print("RECRUITMENT ANALYTICS DATASET")
print("=" * 50)

print("\nDataset Loaded Successfully!")

# Dataset Preview
print("\nFirst 5 Records")
print(df.head())

# Dataset Information
print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())


# Best Match Analysis
print("\nBest Match Distribution")
print(df["Best Match"].value_counts())

selection_rate = (
    df["Best Match"].value_counts(normalize=True) * 100
)

print("\nSelection Percentage")
print(selection_rate)

# Gender Analysis
print("\nGender Distribution")
print(df["Gender"].value_counts())


# Age Analysis
print("\nAge Statistics")
print(df["Age"].describe())

# Top Job Roles
print("\nTop 10 Job Roles")
print(df["Job Roles"].value_counts().head(10))

# VISUALIZATIONS

# Best Match Bar Chart
plt.figure(figsize=(6,4))
df["Best Match"].value_counts().plot(kind="bar")
plt.title("Best Match Distribution")
plt.xlabel("Best Match")
plt.ylabel("Number of Applicants")
plt.show()

# Best Match Pie Chart
plt.figure(figsize=(6,6))
df["Best Match"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Best Match Percentage")
plt.ylabel("")
plt.show()

# Gender Distribution
plt.figure(figsize=(6,4))
df["Gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Applicants")
plt.show()

# Age Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Applicants")
plt.show()

# Top Job Roles
plt.figure(figsize=(10,6))
df["Job Roles"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Job Roles")
plt.xlabel("Job Role")
plt.ylabel("Applicants")
plt.xticks(rotation=45)
plt.show()
print("\nAnalysis Completed Successfully!")