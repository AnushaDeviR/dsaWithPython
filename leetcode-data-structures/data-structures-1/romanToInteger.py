
def romanToInt(self, s: str) -> int:
    
#  create a hash table for roman numbers: 
    romanMap = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    num = 0 

    for i in range(len(s)): 
        # check if there is a character after the numeral 
        if i + 1 < len(s) and romanMap[s[i]] < romanMap[s[i + 1]]:
            num -= romanMap[s[i]]
        else: 
            num += romanMap[s[i]]

    return num
    