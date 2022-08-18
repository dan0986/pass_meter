# Паролеметр - определение уровня рейтинга введенного пароля

При вводе пароля автоматически определяется его рейтинг в баллах (от 1 до 7).
Один балл добавляется:
1. В случае, если длина пароля равна или более 13 символов.
2. В случае, если пароль содержит цифру `[0-9]`.
3. В случае, если пароль содержит букву `[A-Za-z]`.
4. В случае, если пароль содержит заглавную букву `[A-Z]`.
5. В случае, если пароль содержит строчную букву `[a-z]`.
6. В случае, если пароль содержит символы: `~!@#$%^&*()[]-_=+/.,;:"'| `
7. В случае, если пароль содежат не только символы: `~!@#$%^&*()[]-_=+/.,;:"'| `

## Как установить 

`python3` должен быть уже установлен. Рекомендуется использовать виртуальное окружение для изодяции проекта [virtualenv/venv](https://docs.python.org/3/library/venv.html) . Затем используйте `pip` (или `pip3`) для установки зависимостей:

```sh
	pip3 install -r requirements.txt
```

## Пример запуска скрипта
Перейдите в папку проекта и запустите сам скрипт:

```sh
	python3 pass_meter.py
```

Для выхода нужно нажать комбинацию клафиш `CTRL+C`:

## Запуск линтеров

```
tox
```

## Цель проекта

Код написан в образовательных целях.
