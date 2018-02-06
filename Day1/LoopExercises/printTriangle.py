#Solution incomplete for now cause my brain is dead and I wanna go workout

import math

def printTriangle(height):
    row = ""
    for i in range(0, 2* height):
        for j in range(0, 2* height):
            if (j in range(math.ceil(height/2)-1, math.ceil(height/2))):
                row += "*"
            else: 
                row += " "
        print(row)
        row = ""
        
        


printTriangle(7)

