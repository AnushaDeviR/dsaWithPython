# calculate power of a number using recursion
# x = base, n = exponent
def calpower(x, n):
    assert int(n) == n, "Exponent (n) should be an integer"
    if n == 0:
        return 1
    elif n < 0:
        return 1/(x * calpower(x, n+1))
    else:
        return x * calpower(x, n-1)


print(calpower(2, -3))
