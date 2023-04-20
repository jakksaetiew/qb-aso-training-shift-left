import matplotlib.pyplot as plt
import pandas as pd


def load_data(url: str) -> pd.DataFrame:
    """
    Load data from a URL into a Pandas DataFrame.

    Args:
        url: The URL of the data file.

    Returns:
        A Pandas DataFrame containing the loaded data.
    """
    return pd.read_csv(url)


def plot_histogram(data: pd.Series) -> None:
    """
    Plot a histogram of a given Pandas Series.

    Args:
        data: The Pandas Series to plot the histogram of.
    """
    plt.hist(data)
    plt.show()


def aggregate_data(data: pd.DataFrame, groupby_col: str, agg_col: str) -> pd.DataFrame:
    """
    Aggregate a given Pandas DataFrame by a given column and compute the mean of
    another column.

    Args:
        data: The Pandas DataFrame to aggregate.
        groupby_col: The name of the column to group by.
        agg_col: The name of the column to compute the mean of.

    Returns:
        A Pandas DataFrame containing the aggregated data.
    """
    grouped_df = data.groupby(groupby_col).agg({agg_col: "mean"})
    return grouped_df


def plot_bar_chart(data: pd.DataFrame) -> None:
    """
    Plot a bar chart of a given Pandas DataFrame.

    Args:
        data: The Pandas DataFrame to plot the bar chart of.
    """
    data.plot(kind="bar")
    plt.show()


if __name__ == "__main__":
    # Load sample data
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    df = load_data(url)

    # Show first 5 rows of the data
    print(df.head())

    # Check the data types of each column
    print(df.dtypes)

    # Convert the 'sex' column to category type
    df["sex"] = df["sex"].astype("category")

    # Plot the distribution of total bill amount
    plot_histogram(df["total_bill"])

    # Aggregate the data by sex and compute the average total bill
    grouped_df = aggregate_data(df, "sex", "total_bill")
    print(grouped_df)

    # Plot the average total bill by sex
    plot_bar_chart(grouped_df)
