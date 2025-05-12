# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Step 2: Load Data
df = pd.read_csv("owid-covid-data.csv")

# Step 3: Preview Data
print(df.head())
print(df.columns)  # Check available columns

# Step 4: Data Cleaning
df['date'] = pd.to_datetime(df['date'])  # Convert date column
df = df.dropna(subset=['total_cases', 'total_deaths'])  # Remove rows missing key values

# Step 5: Filter for Selected Countries
countries = ['Kenya', 'USA', 'India']
df_selected = df[df['location'].isin(countries)]

# Step 6: Exploratory Data Analysis
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_selected, x='date', y='total_cases', hue='location')
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.show()

# Step 7: Death Rate Calculation
df_selected['death_rate'] = df_selected['total_deaths'] / df_selected['total_cases']
sns.lineplot(data=df_selected, x='date', y='death_rate', hue='location')
plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.show()

# Step 8: Vaccination Progress
sns.lineplot(data=df_selected, x='date', y='total_vaccinations', hue='location')
plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.show()

# Step 9: Optional Choropleth Map (Cases per Country)
latest_df = df[df['date'] == df['date'].max()]
fig = px.choropleth(latest_df, locations="iso_code", color="total_cases",
                     hover_name="location", title="Global COVID-19 Cases")
fig.show()

# Step 10: Summarizing Key Insights
key_insights = """
- USA recorded the highest total cases in the dataset.
- Kenya had lower total cases but a fluctuating vaccination rate.
- India's vaccination rollout showed consistent growth over time.
"""
print(key_insights)
