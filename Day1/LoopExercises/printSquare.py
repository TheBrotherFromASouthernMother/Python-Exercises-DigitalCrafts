def printSquareWithSpaces(size):
    for i in range (0, size):
        for j in range (0, size):
            print("*", end=" ")
        print(" ")
    

printSquareWithSpaces(5)




def printSquareWithoutSpaces(size):
    for i in range (0, size):
        row = ""
        for j in range (0, size):
            row += "*"
        print(row)


printSquareWithoutSpaces(5)