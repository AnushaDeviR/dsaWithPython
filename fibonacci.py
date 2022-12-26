def fibonacci(n):
    assert n >= 0 and int(
        n) == n, "Fibonacco number cannot be a negative number or non integer"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(100))
