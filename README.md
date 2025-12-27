# Password Generator / Validator
Учебный проект на Python.
## Возможности
- генерация безопасных паролей
- проверка сложности пароля
- запуск через CLI

## Требования
Python 3.10+

## Установка
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Использование
Генерация пароля
python -m cli.main --generate --length 16
Проверка пароля
python -m cli.main --validate MyPassword123!
Правила пароля
длина минимум 8
есть строчная буква
есть заглавная буква
есть цифра
есть спецсимвол
нет неоднозначных символов (0 O 1 l I)
Автор
Студент (1 человек, Python)
