import random
import string
from .rules import SYMBOLS, AMBIGUOUS


def generate_password(
    length=12,
    use_digits=True,
    use_symbols=True,
    use_upper=True,
    avoid_ambiguous=True
):
    chars = list(string.ascii_lowercase)

    if use_upper:
        chars += list(string.ascii_uppercase)

    if use_digits:
        chars += list(string.digits)

    if use_symbols:
        chars += list(SYMBOLS)

    if avoid_ambiguous:
        chars = [c for c in chars if c not in AMBIGUOUS]

    return "".join(random.choice(chars) for _ in range(length))
