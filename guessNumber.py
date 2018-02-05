import random





def guessingGame():
    secret_number = random.randint(1, 10)
    numberOfGuesses = 5
    print("I am thinking of  a number between 1 and 10")
    guess = int(input("What's the number? "))
    while (guess != secret_number):
        numberOfGuesses -= 1
        if numberOfGuesses < 1:
            print("You ran out of guesses :(")
            break
        if guess > secret_number:
            print("hmmmm that's a little too high")
        elif guess < secret_number:
            print("Just a little bit too low")
        print("you have {} guesses left".format(numberOfGuesses))
        guess = int(input("What's the number? "))
        
    else:
        print("Yes! You win!")

guessingGame()

playAgain = str(input("Wanna play again? (Y or N) ")).upper()

while playAgain == "Y":
    guessingGame()
    playAgain = str(input("Wanna play again? (Y or N) ")).upper()