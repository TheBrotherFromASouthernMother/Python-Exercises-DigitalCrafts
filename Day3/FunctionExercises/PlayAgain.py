def wannaPlayAGame():
        userAnswer = str(input("Wanna play again?(Y or N): ")).upper()
        if userAnswer == "Y":
            return True
        elif userAnswer == "N":
            return False
        else:
            while(userAnswer != "N" and userAnswer != "Y"):
                userAnswer = str(input("Wanna play again?(Y or N) ")).upper()


if __name__ == "__main__":
    wannaPlayAGame()