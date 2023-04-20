from typing import Any, Union

import pandas as pd


def transform_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    def lowercase_str(x: Union[str, Any]) -> Union[str, Any]:
        return x.lower() if isinstance(x, str) else x

    # Convert all string columns to lowercase
    # Drop all rows that have NaN values
    # Reset the index of the DataFrame

    return df.applymap(lowercase_str).dropna().reset_index(drop=True)
