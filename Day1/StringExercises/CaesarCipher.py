import math

userString = str(input("Give me a string you'd like to encrypt: ")).upper()
userKey = int(input("Give me an encryption key (number between 1-26): "))

def cipher(string, key):
    encryptedString = ""
    placeholder = 0
    for i in string:
        if i != " " or i != "." or i != "!" or i != "?":
            placeholder = ord(i) 
           
            if placeholder + key > 91:
                placeholder = (((placeholder - 65) + key) % 26) + 65
                print(placeholder)
            else:
                placeholder = placeholder + key
                
                print(placeholder)
            encryptedString += chr(placeholder)
    return encryptedString


print(cipher(userString, userKey))