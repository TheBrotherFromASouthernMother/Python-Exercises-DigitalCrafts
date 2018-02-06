width = int(input("Please select a width in whole numbers: "))
height = int(input("Please select a height in whole numbers: "))
print(width-1)

for i in range (0, height):
        row = ""
        for j in range (0, width):
            if (i < 1 or i == height-1) or (j < 1 or j == width-1): 
                row += "*"
            else:
                 row += " "
        print(row)
        row = ""