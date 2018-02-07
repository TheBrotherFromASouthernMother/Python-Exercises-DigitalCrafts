



def triangleNumbers():
    stepVal = 0
    numIterations = range(0, 101) #101 iterations
    for i in range(len(numIterations)):
        if (stepVal + i) >= len(numIterations):
            break
        else:
            print("Triangle Numbers: {}".format(numIterations[stepVal + i]), " stepVal: {}  i: {}".format(stepVal, i)) #i.e. (stepValue == 0 i == 0 produces 0), (stepValue == 0, i == 1 produces 1), (stepValue == 1, i == 2 produces 3) (stepValue == 3, i == 3 produces 6), etc.
            stepVal += i

triangleNumbers()



    #might require a recursive solution


# def printTriangleNumbers(num):
#     i = 1 + num
#     if i >= 100:
#         return True
#     print(i)
#     printTriangleNumbers(num + num)


# printTriangleNumbers(1)