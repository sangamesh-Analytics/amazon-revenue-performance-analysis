import pandas as pd

df = pd.read_csv('Ban_Data.csv')

print(df.shape)
print(df.columns)
print(df.head())

print(df.isnull().sum())

df[df.astype(str).apply(lambda x: x.str.contains(r"\?{2,}")).any(axis=1)].head()

df_clean = df.dropna(subset=[
    'category_title',
    'ward_title',
    'created_at'
])

print(df_clean.shape)

df_clean['category_title'].value_counts().head(10)
print(df_clean['category_title'].value_counts().head(10))

# Complaint categories - Visual 1
import matplotlib.pyplot as plt

top_categories = df_clean['category_title'].value_counts().head(10)

plt.figure(figsize=(10,6))
top_categories.plot(kind='bar')

plt.title("Top Complaint Categories in Bangalore")
plt.xlabel("Complaint Category")
plt.ylabel("Number of Complaints")

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig("complaint_categories.png", dpi=300)  # saves the image
plt.show()


print(df_clean['ward_title'].value_counts().head(10))

top_wards = df_clean['ward_title'].value_counts().head(10)

#Complaint Hotspots - Visual 2
import matplotlib.pyplot as plt

top_wards = df_clean['ward_title'].value_counts().head(10)

plt.figure(figsize=(10,6))
top_wards.plot(kind='bar')

plt.title("Top Wards with Highest Civic Complaints")
plt.xlabel("Ward")
plt.ylabel("Number of Complaints")

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig("complaints_by_ward.png", dpi=300)
plt.show()


df_clean['created_at'] = pd.to_datetime(df_clean['created_at'], format='mixed', dayfirst=True)

complaints_by_date = df_clean.groupby(df_clean['created_at'].dt.date).size()

#Cmplaint Trnds Over Time - Visual 3
import matplotlib.pyplot as plt

complaints_by_date = df_clean.groupby(df_clean['created_at'].dt.date).size()

plt.figure(figsize=(10,6))
complaints_by_date.plot()

plt.title("Trend of Civic Complaints Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Complaints")

plt.tight_layout()

plt.savefig("complaint_trend.png", dpi=300)
plt.show()

print(df_clean['complaint_status_title'].value_counts())
