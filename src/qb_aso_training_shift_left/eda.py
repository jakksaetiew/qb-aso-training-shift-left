# %%
import matplotlib.pyplot as plt
import pandas as pd

# Load sample data
df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
)

# Show first 5 rows of the data
df.head()

# %%
# Check the data types of each column
df.dtypes

# %%
# Convert the 'sex' column to category type
df["sex"] = df["sex"].astype("category")

# %%
# Plot the distribution of total bill amount
plt.hist(df["total_bill"])
plt.show()

# %%
# Aggregate the data by sex and compute the average total bill and tip
grouped_df = df.groupby("sex").agg({"total_bill": "mean", "tip": "mean"})
grouped_df

# %%
# Plot the average total bill and tip by sex
grouped_df.plot(kind="bar")
plt.show()
# %%
