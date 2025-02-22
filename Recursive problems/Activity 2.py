def reversestring(s):
    if len(s) ==1:
        return s[0]
    
    firstcharacter = s[0]
    return reversestring(s[1:]) + firstcharacter

s = input("Enter some characters")
print(reversestring(s))