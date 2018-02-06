numberOfCoins = 0
offer = str(input("Do you want a coin? ")).upper()

while offer != "NO":
    if (offer == "YES"):
        numberOfCoins += 1
        print("You have {} coins".format(numberOfCoins))
    offer = str(input("Do you want another? " )).upper()
else:
    print("Bye")
