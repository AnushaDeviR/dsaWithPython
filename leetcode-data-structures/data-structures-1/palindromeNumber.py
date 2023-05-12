def isPalindrome(self, x: int) -> bool:

    '''brute-force
    if str(x)[::-1] == str(x):              
        return True
    else:
        return False
    '''

    if x < 0: 
        return False
    reverse = 0
    temp = x
    while x > 0:
        lastDigit = x % 10
        reverse = reverse * 10 + lastDigit
        x = x // 10
    return reverse == temp
