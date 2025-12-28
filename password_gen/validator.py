from .rules import MIN_LENGTH, GOOD_LENGTH, SYMBOLS
def validate_password(password: str):
    score = 0
    feedback = []

    if len(password) >= MIN_LENGTH:
        score += 1
    else:
        feedback.append("Пароль слишком короткий")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Добавьте цифры")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Добавьте буквы в верхнем регистре")

    if any(c in SYMBOLS for c in password):
        score += 1
    else:
        feedback.append("Добавьте спецсимволы")

    if len(password) >= GOOD_LENGTH:
        score += 1

    levels = {
        0: "очень слабый",
        1: "слабый",
        2: "ниже среднего",
        3: "нормальный",
        4: "сильный",
        5: "очень сильный"
    }

    return levels[score], feedback
