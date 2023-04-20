from qb_aso_training_shift_left.main import be_polite


def test_be_polite() -> None:
    msg = be_polite()
    msg.should.equal("Hi Mom!")
