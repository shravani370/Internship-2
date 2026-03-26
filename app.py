import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

print(df.head())
print(df.info())
print(df.describe())

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Score'] = df['Score'].fillna(df['Score'].mean())
df['City'] = df['City'].fillna(df['City'].mode()[0])

df = df.drop_duplicates()

df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')

print(df)

df['City'].value_counts().plot(kind='bar')
plt.title("Count of Students by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()

plt.hist(df['Age'], bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df['Age'], df['Score'])
plt.title("Age vs Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.show()

plt.boxplot(df['Score'])
plt.title("Boxplot of Scores")
plt.ylabel("Score")
plt.show()

corr = df.corr(numeric_only=True)

plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.show()