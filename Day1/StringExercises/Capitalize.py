userString = str(input("Give me a string: "))

def CapitalizeString(string):
    capitalizedString = string[0].upper()
    modifiedString = string[1:]
    modifiedString = capitalizedString + modifiedString
    return modifiedString


print(CapitalizeString(userString))


