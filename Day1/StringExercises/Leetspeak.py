userString = str(input("Give me a string and I'll convert it to leet l337 speak: ")).upper()

def makeLeetSpeak(string):
    modifiedString = ""
    for i in string:
        if i == "A":
            modifiedString += "4"
        elif i == "E":
            modifiedString += "3"
        elif i == "G":
            modifiedString += "6"
        elif i == "O":
            modifiedString += "0"
        elif i == "S":
            modifiedString += "5"
        elif i == "T":
            modifiedString += "7"
        else:
            modifiedString += i
    return modifiedString

print(makeLeetSpeak(userString))