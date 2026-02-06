def apply_twice(f, x):
    """Применяет функцию f к x дважды.
    
    >>> apply_twice(lambda x: x + 1, 5)
    7
    >>> apply_twice(lambda x: x * 2, 3)
    12
    >>> apply_twice(lambda x: x * x, 2)
    16.
    """
    return f(f(x))
