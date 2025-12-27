from password_gen.generator import generate_password


def test_password_length():
    pwd = generate_password(length=20)
    assert len(pwd) == 20
