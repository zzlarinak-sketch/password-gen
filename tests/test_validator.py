from password_gen.validator import validate_password


def test_short_password_is_weak():
    level, _ = validate_password("abc")
    assert level == "очень слабый"

