from drawShapes import *


speed(5)
#middle
drawShapeInverted(3, 50, -50, 55, "grey", True)
drawShape(3, 50, -10, 10, "#636366", True)
drawShape(3, 50, -50, 65, "#1b81c5", True)
drawShapeInverted(3, 50, -85, 110, "#1478aa", True)

#green arm
drawShape(3, 50, -120, 65, "#3c6d5a", True)
drawShapeInverted(3, 50, -155, 110, "#83be37", True )
drawParallelogram(5, -155, 120, "#517e37", True)
drawRhombus(5, -265, 120, "#71ba3a", True)

#blue arm
drawShapeInverted(3, 50, -120, 55, "#145b99", True)
drawShape(3, 50, -155, 10, "#1d88f0", True)
drawParallelogramInverted(5, -155, -5, "#0c64af", True)
drawRhombusInverted(5, -265, -5, "#1c82c3", True)


#grey arm
drawShape(3, 50, 15, 60, "#888a8c", True)
drawShapeInverted(3, 50, 50, 105, "#b3b5b7", True)
drawParallelogramInverted(5, 60, 170, "#9ca0a1", True)
drawRhombus(5, 110, 115, "#b3b5b7", True)


#orange arm
drawShapeInverted(3, 50, 30, 50, "#ba764a", True)
drawShape(3, 50, 70, 10, "#fca916", True)
drawParallelogram(5, 75, -60, "#f26c1e", True)
drawRhombusInverted(5, 125, -5, "#f8941d", True)


mainloop()



