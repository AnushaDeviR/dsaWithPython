# Sum of digits of a postive integer number using recursion

def positivesum(n):
    assert n >= 0 and int(n) == n, "Number is not positive"
    if n//10 == 0:
        return int(n)
    else:
        return positivesum(int(n//10)) + int(n % 10)


print(positivesum(-10))
