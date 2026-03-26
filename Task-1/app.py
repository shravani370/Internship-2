import pandas as pd

df = pd.read_csv("student_data.csv")

#Looking at the data
print(df.isnull().sum())

#Flling the missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Score'] = df['Score'].fillna(df['Score'].mean()).round(2)
df['City'] = df['City'].fillna(df['City'].mode()[0])

#Drop Duplicates
df = df.drop_duplicates()

#Fixing the joining dates
def fix_date(date):
    if pd.isnull(date):
        return None
    
    date = str(date)
    
    if len(date) >= 10 and date[4] == '-':
        d = pd.to_datetime(date, format='%Y-%m-%d', errors='coerce')
    else:
        d = pd.to_datetime(date, dayfirst=True, errors='coerce')
    
    if pd.isnull(d):
        return None
    
    return d.strftime('%d-%m-%Y')

df['Join_Date'] = df['Join_Date'].apply(fix_date)

df = df.dropna(subset=['Join_Date'])

print(df.isnull().sum())
print(df.head())

df.to_csv("cleaned_data.csv", index=False)
