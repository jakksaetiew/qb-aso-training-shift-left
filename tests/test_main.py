import pandas as pd
from pandas.testing import assert_frame_equal

from qb_aso_training_shift_left.main import be_polite, transform


def test_be_polite() -> None:
    msg = be_polite()
    msg.should.equal("Hi Mom!")


def test_transform_should_do_nothing() -> None:
    df_test = pd.DataFrame(
        columns=["a", "b", "c"],
        data=[
            [1, 2, 3],
            [2, 3, 4],
        ],
    )
    actual = transform(df_test)
    expected = df_test

    assert_frame_equal(actual, expected)
