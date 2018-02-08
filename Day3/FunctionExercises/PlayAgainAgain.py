def wannaPlayAGame():
        userAnswer = str(input("Wanna play again?(Y or N): ")).upper()
        if userAnswer == "Y":
            return True
        elif userAnswer == "N":
            return False
        else:
            while(userAnswer != "N" and userAnswer != "Y"):
                userAnswer = str(input("INVALID INPUT TYPE(Y or N): ")).upper()


wannaPlayAGame()