import pandas as pd


def be_polite() -> str:
    msg = "Hi Mom!"
    return msg


def transform(df: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df, df]).drop_duplicates().reset_index(drop=True)


if __name__ == "__main__":
    be_polite()
