
## Формат задачи
**description.json:**
```json
{
    "title": ""

    "problem": {
        "text": "",
        "answer": ""
    },

    "solution": {
        "text": "",
        "answer": ""
    }
}
```

**Необязательные поля:**
- `problem.answer` - Плейсхолдер в поле ответа
- `solution.text` - Запятые меняются на точки автоматически

**Структура репозитория:**
```
root/
    tests/
        <test-ID: int>/
            description.json
        <test-ID: int>/
            description.json
        ...
    README.md
```
