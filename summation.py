def summation(n, term):
    """Возвращает сумму term(1) + term(2) + ... + term(n).
    
    >>> summation(5, lambda x: x)
    15
    >>> summation(5, lambda x: x * x)
    55
    >>> summation(3, lambda x: x ** 3)
    36
    """
    resalt = 0
    k = 1
    while n >= k:
        resalt += term(k)
        k += 1
    return resalt




