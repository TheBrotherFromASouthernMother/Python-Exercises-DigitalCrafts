import math

userString = str(input("Give me a string you'd like to encrypt: ")).upper()
#This is the user inputed string that will be encrypted

"""Will parse the string into individual chars, shift them by a given amount between
1 and 26, recompile them into an encrypted or decrypted string"""
def cipher(string, key):
    encryptedString = ""
    charToEncrypt = 0
    for i in string:
        if i != " " or i != "." or i != "!" or i != "?":
            charToEncrypt = ord(i) 
           
            if charToEncrypt + key > 90:
                """This is necessary in order to make sure the string stays encrypted to be
                only alphanumerical character, otherwise you can get an encrypted string
                that has a bunch of random symbols, which makes it way harder to decrypt"""
                charToEncrypt = (((charToEncrypt - 65) + key) % 26) + 65
            else:
                charToEncrypt = charToEncrypt + key
                
            encryptedString += chr(charToEncrypt)
    return encryptedString


#To test that the cipher function is working, leave commented out otherwise
# print(cipher(userString, 13))


"""Calls the cipher function over and over again printing all possible shifts of the given
encrypted string "lbh zhfg hayrnea jung lbh unir yrnearq" which at a shift of 13 comes out
as "You-Must-Unlearn-What-You-Have-Learned." It should print that with spaces instead
of hyphens however I can't quite figure out the math necessary to get it to do so."""

def bruteForceCheck(someFunction):
    for i in range(1, 27):
        print(i, someFunction(userString, i), "\n\n")


bruteForceCheck(cipher)