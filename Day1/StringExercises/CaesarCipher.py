userString = str(input("Give me a string you'd like to encrypt: "))

def cipher(string):
    encryptedString = ""
    placeholder = 0
    for i in string:
        if i != " " or i != "." or i != "!" or i != "?":
            placeholder = ord(i) 
            print(placeholder)


cipher(userString)