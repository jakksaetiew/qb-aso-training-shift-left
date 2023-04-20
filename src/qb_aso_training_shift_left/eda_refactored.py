# %%
from qb_aso_training_shift_left.eda_utils import (
    aggregate_data,
    load_data,
    plot_bar_chart,
    plot_histogram,
)

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = load_data(url)

# %%
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
plot_histogram(df["total_bill"])

# %%
# Aggregate the data by sex and compute the average total bill
grouped_df_bill = aggregate_data(df, "sex", "total_bill")
grouped_df_bill

# %%
# Plot the average total bill by sex
plot_bar_chart(grouped_df_bill)

# %%
# Aggregate the data by sex and compute the average total bill
grouped_df_tip = aggregate_data(df, "sex", "tip")
grouped_df_tip

# %%
# Plot the average total bill by sex
plot_bar_chart(grouped_df_tip)

# %%
