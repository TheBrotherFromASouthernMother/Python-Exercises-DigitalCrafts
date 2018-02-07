import math
userHeight = int(input("Please input the height of a triangle(Must Be greater than 6): "))

def printTriangle(height):
    if height < 6: 
        height = height * 2
    row = []
    for i in range(0,height):
        row.append(" ")
    j = math.floor(int(height / 2))
    k = math.floor(int(height / 2))
    while j < height and k > 0:
        row[j] = "*"
        row [k] = "*"
        string = ""
        print(string.join(row))
        j += 1
        k -= 1


#Solution to printTriangle
printTriangle(10)

#Solution to printTriangleII
printTriangle(userHeight)