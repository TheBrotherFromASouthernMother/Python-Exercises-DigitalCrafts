
#GuessingGameII

#Planning Stage:
#Sounds like a binary search?
#num = range(1, 101)
#guess = math.floor((min + max)/2)
#program would have to multiple times if num[guess] is equal, greather tha, or less than the user's chosen num
#would probably be a while loop that breaks if num[guess] is equal, or if min > max
#maybe create a case condition if the user is a dirty liar, like force them to the num beforehand?




#Implemnatation: 
import math
numRange = range(1, 101)

def guessUserNumber():
    guessCount = 1
    print("Think of a number between 1 and 100 and I'll guess it")
    min = 0
    max = len(numRange) -1
    while (max > min):
        guessCount += 1
        guess = math.floor((max + min) / 2 )
        print("Current Guess: %d" % guess)
        userNum = str(input("Is this your number?, (Print:\'yes\', \'high\', \'low\'): ")).upper()
        if (userNum == "LOW"):
            min = guess + 1
        elif (userNum == "HIGH"):
            max = guess - 1
        elif (userNum == "YES"):
            print("YES I GUESSED YOUR NUMBER!")
            return True
            break
        print("Guess Count: %d" % (guessCount))
    else:
        print("Sorry I couldn't find your number ", "\U0001F641")
        return False


guessUserNumber()
