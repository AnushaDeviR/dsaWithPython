'''
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode


Example 1:
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]

Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example 2:
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]

Explanation:
One possible encode method is: "we:;say:;:::;yes"
'''
def decode(strs):

    # 1. Encode each word in the input with its length and a delimiter (;) before it and return it as a string: 

    encodedString = ""

    for s in strs:
        encodedString += str(len(s)) + ";" + s

    print("encoded: ", encodedString)

    res = []
    l = 0 

    # Decoding:
    # By using 2 pointers approach: set left pointer to 0th index and right pointer at left pointer 
    while l < len(encodedString):
        r = l 
        # if delimiter found then increment r pointer
        while encodedString[r] != ";":
            r += 1

        # find the length of the encoded words in the string 
        length = int(encodedString[l:r])

        # append each word into the result array
        res.append(encodedString[r+1: r + 1 + length])

        # update the left pointer to the position before the next set of encoded word
        l = r + 1 + length

    return res

input = ["we;", "say", ":", "yes"]

print(decode(input))
