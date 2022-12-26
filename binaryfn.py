def bintodec(n):
    assert int(n) == n, "Input must be an integer"
    if n//2 == 0:
        return 1
    else:
        return bintodec(int(n//2))*10 + int(n) % 2


print(bintodec(13))
