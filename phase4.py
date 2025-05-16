import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("your_file.csv")

# Sample first 10 rows for visualization
sample_df = df.head(10)

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Bar chart: Date vs Volume
ax1.bar(sample_df['date'], sample_df['volume'], color='red')
ax1.set_title('Bar Chart: Volume Over Time')
ax1.set_xlabel('Date')
ax1.set_ylabel('Volume')
ax1.tick_params(axis='x', rotation=45)

# Scatter plot: Open vs Close
ax2.scatter(sample_df['open'], sample_df['close'], color='blue')
ax2.set_title('Scatter Plot: Open vs Close Prices')
ax2.set_xlabel('Open Price')
ax2.set_ylabel('Close Price')

plt.tight_layout()
plt.show()
