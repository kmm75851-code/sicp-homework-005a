# Домашка 005a - Higher Order (Basics)

Функции как аргументы.

## Задание

### Файл 1: `apply_twice.py`

```python
def apply_twice(f, x):
    """Применяет функцию f к x дважды."""
    # твой код здесь
```

**Примеры:**
- `apply_twice(lambda x: x + 1, 5)` → 7
- `apply_twice(lambda x: x * 2, 3)` → 12
- `apply_twice(lambda x: x * x, 2)` → 16

### Файл 2: `summation.py`

```python
def summation(n, term):
    """Возвращает сумму term(1) + term(2) + ... + term(n)."""
    # твой код здесь
```

**Примеры:**
- `summation(5, lambda x: x)` → 15
- `summation(5, lambda x: x*x)` → 55

## Как сдать

1. Форкни этот репозиторий
2. Реализуй функции
3. `pytest tests/ -v`
4. Commit и push
5. Проверь Actions ✅

## Ключевые концепции

- **Lambda:** `lambda x: x * 2` — анонимная функция
- **Функция высшего порядка** — принимает функции как аргументы
