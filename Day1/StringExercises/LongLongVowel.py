userString = str(input("Give me a word with an extended vowel (Ex. \'Cheese\'): "))

def extendVowel(string):
    modifiedString = ""
    for i in range(0, len(string)):
        if string[i] == string[i-1]:
            modifiedString += (string[i] * 4)
        modifiedString += string[i]
    return modifiedString

print(extendVowel(userString))
