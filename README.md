
## Формат задачи
**description.json:**
```json
{
    "title": "",

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
- `problem.answer` - Плейсхолдер в поле ответа.
- `solution.answer` - Запятые меняются на точки автоматически, регистр неважен.

Актуальный формат: [`MathTest.js`](https://github.com/nkg-17/math-tests-tv/blob/main/src/common/MathTest.js), [`util.js`](https://github.com/nkg-17/math-tests-tv/blob/main/src/api/util.js) (может измениться)

## Структура репозитория
```
root/
    tests/
        <ID>/
            description.json
        <ID>/
            description.json
        ...
    README.md
```
- `ID` - Неповторяющееся число или строка ([формат](https://github.com/nkg-17/math-tests-tv/blob/cb6ad52c47a8085fa9690786cccc11119293066e/src/common/MathTest.js#L62))
