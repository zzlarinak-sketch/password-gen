# Password Generator / Validator
Учебный проект на Python.
## Возможности
- генерация безопасных паролей
- проверка сложности пароля
- запуск через CLI

## Требования
Python 3.10+

## Установка

python3 -m venv venv
source venv/bin/activate
pip install -e

## Использование
Генерация пароля
python -m cli.main --generate --length 16
Проверка пароля
python -m cli.main --validate MyPassword123!
## Правила пароля
длина минимум 8
есть строчная буква
есть заглавная буква
есть цифра
есть спецсимвол
нет неоднозначных символов (0 O 1 l I)
## Тесты
pytest
## CI
В проекте настроен CI с помощью GitHub Actions:
запуск flake8;
запуск pytest при каждом push и pull request.
## Git Flow
Используется базовый git flow:
main — стабильная версия;
develop — активная разработка;
изменения вносятся через отдельные коммиты с осмысленными сообщениями.
