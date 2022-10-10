# Архив задач по стереометрии ЕГЭ

## Шаблон файла задачи
```json
{

    "11375": { 
        "name": "Объём цилиндра",
        "tags": [ "объём" ],
        "problem": {
            "preface": "Цилиндр и конус имеют общие основание и высоту. Объём конуса равен 25.",
            "tasks": [
                { 
                    "title": "Найти",
                    "text": "объём цилиндра"
                }
            ],
            "pictureUrl": "problem-picture.png"
        },
        "solution": {
            "preface": "Текст решения",
            "tasks": [
                {
                    "text": "Текст решения 1-ой подзадачи",
                    "answer": "Ответ к 1-ой подзадаче"
                }
            ],
            "pictureUrl": "solution-picture.png"
        }
    }

}
```
Поле `pictureUrl` содержит путь к рисунку задания относительно файла `description.json`.

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







