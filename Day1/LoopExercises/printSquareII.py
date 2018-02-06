userSpecifiedSize = int(input("Please select a size: "))

def printSquareWithSpaces(size):
    for i in range (0, size):
        for j in range (0, size):
            print("*", end=" ")
        print(" ")
    

printSquareWithSpaces(userSpecifiedSize)




def printSquareWithoutSpaces(size):
    for i in range (0, size):
        row = ""
        for j in range (0, size):
            row += "*"
        print(row)


printSquareWithoutSpaces(userSpecifiedSize)