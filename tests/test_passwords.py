from password_gen.generator import generate_password
from password_gen.validator import validate_password


def test_generated_password_valid():
    pwd = generate_password(length=12)
    assert validate_password(pwd)


def test_generated_password_length():
    pwd = generate_password(length=20)
    assert len(pwd) == 20
