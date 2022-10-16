# Архив задач по стереометрии ЕГЭ

## Шаблон файла описания задачи
```json
{
    "name": "Объём цилиндра",
    "tags": [ "объём", "цилиндры" ],
    "starred": true,
    "problem": {
        "preface": "Цилиндр и конус имеют общие основание и высоту. Объём конуса равен 25.",
        "tasks": [
            { "title": "Найти", "text": "Длину стороны а." },
            { "title": "Найти", "text": "Объём цилиндра." },
            { "title": "Доказать", "text": "Стороны а и b равны" }
        ],
        "pictureUrl": "problem-picture.svg"
    },
    "solution": {
        "preface": "Сдесь мы начинаем решать задачу.",
        "tasks": [
            { "text": "Так находим длину стороны а.",   "answer": "5 см." },
            { "text": "Находим объём цилиднра",         "answer": "3 м^3" },
            { "text": "Доказываем равенство сторон а и b" }
        ],
        "pictureUrl": "solution-picture.png"
    }
}
```
Поле `pictureUrl` содержит путь к рисунку задания относительно файла `description.json`. Поле `solution.pictureUrl` *не объязательно*, по умолчанию используется `problem.pictureUrl`. Поле `solution.tasks.answer` также может отсутствовать.

## Структура папок репозитория
```
/
    README.md
    tests/
        11375/
            description.json
            problem-picture.png
            solution-picture.png
        88501/
            description.json
            ...
        52910/
            description.json
            ...
```







