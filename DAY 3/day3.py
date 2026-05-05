import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (NASA Exoplanet Archive sample)
url = "https://raw.githubusercontent.com/OpenExoplanetCatalogue/oec_tables/master/comma_separated/open_exoplanet_catalogue.txt"

# Read data
df = pd.read_csv(url)

# Show basic info
print("Dataset shape:", df.shape)
print(df.head())

# Clean data: keep important columns
print(df.columns.tolist())
df = df[['name', 'radius', 'period', 'system_distance']]
# Drop missing values
df = df.dropna()

# Rename columns for clarity
df.columns = ['Planet', 'Radius (Jupiter)', 'Orbit Period (days)', 'Distance (light years)']

print("\nCleaned Data:")
print(df.head())

# --- Visualization 1: Planet Radius Distribution ---
plt.figure()
sns.histplot(df['Radius (Jupiter)'], bins=30)
plt.title("Distribution of Exoplanet Sizes")
plt.xlabel("Radius (Jupiter units)")
plt.ylabel("Count")
plt.show()

# --- Visualization 2: Distance vs Radius ---
plt.figure()
sns.scatterplot(
    x='Distance (light years)', 
    y='Radius (Jupiter)', 
    data=df
)
plt.title("Planet Size vs Distance from Earth")
plt.show()

# --- Fun Insight ---
big_planets = df[df['Radius (Jupiter)'] > 1]
print("\nNumber of planets bigger than Jupiter:", len(big_planets))