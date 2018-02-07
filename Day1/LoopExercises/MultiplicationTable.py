"""Print the multiplication table for numbers from 1 up to 10."""

def printMutiplicationTable():
    for i in range (1, 11):
        print("\n")
        for j in range (1, 11):
            product = i * j
            print("{0} X {1} = {2}".format(i, j, product))

printMutiplicationTable()