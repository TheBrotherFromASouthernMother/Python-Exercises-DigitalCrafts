userString = str(input("Give me a string: "))

def reverseString(string):
    modifiedString = ""
    for i in range(len(string)-1, -1, -1):
        print(i, string[i])
        modifiedString += string[i]
    return modifiedString

print(reverseString(userString))