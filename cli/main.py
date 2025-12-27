import argparse
from password_gen.generator import generate_password
from password_gen.validator import validate_password


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--validate")
    parser.add_argument("--length", type=int, default=12)

    args = parser.parse_args()

    if args.generate:
        print(generate_password(length=args.length))

    if args.validate:
        level, tips = validate_password(args.validate)
        print("Сложность:", level)
        if tips:
            print("Рекомендации:")
            for t in tips:
                print("-", t)


if __name__ == "__main__":
    main()

