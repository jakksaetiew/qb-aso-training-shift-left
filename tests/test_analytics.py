import pandas as pd
from pandas.testing import assert_frame_equal

from qb_aso_training_shift_left.analytics import transform_dataframe


def test_transform_dataframe() -> None:
    # Test case 1: dataframe with mixed data types
    df1 = pd.DataFrame(
        {"A": [1, 2, 3], "B": ["Foo", "Bar", "FUZZ"], "C": [True, False, True]}
    )
    df1_transformed = transform_dataframe(df1)
    expected_df1 = pd.DataFrame(
        {"A": [1, 2, 3], "B": ["foo", "bar", "fuzz"], "C": [True, False, True]}
    )
    assert_frame_equal(df1_transformed, expected_df1)

    # Test case 2: dataframe with all NaN values
    df2 = pd.DataFrame({"A": [pd.NA, pd.NA, pd.NA], "B": [None, None, None]})
    df2_transformed = transform_dataframe(df2)
    expected_df2 = pd.DataFrame({"A": [], "B": []}).astype(
        {"A": "object", "B": "object"}
    )
    assert_frame_equal(df2_transformed, expected_df2)

    # Test case 3: dataframe with string columns already in lowercase
    df3 = pd.DataFrame({"A": ["foo", "bar"], "B": ["baz", "qux"]})
    df3_transformed = transform_dataframe(df3)
    assert_frame_equal(df3_transformed, df3)

    # Test case 4: dataframe with string columns and NaN values
    df4 = pd.DataFrame({"A": ["FOO", None, "Bar"], "B": ["BAZ", "qux", None]})
    df4_transformed = transform_dataframe(df4)
    expected_df4 = pd.DataFrame({"A": ["foo"], "B": ["baz"]})
    assert_frame_equal(df4_transformed, expected_df4)

    # Test case 5: empty dataframe
    df5 = pd.DataFrame()
    df5_transformed = transform_dataframe(df5)
    assert_frame_equal(df5_transformed, df5)
