matrix1 = [
    [1, 3],
    [2, 4]
]

matrix2 = [
    [5, 2],
    [1, 0]
]

def addMatrices(matrixUno, matrixDos):
  sumOfMatrices = matrixUno
  for i in range(0, len(sumOfMatrices)):
    for j in range(0, len(sumOfMatrices)):
            sumOfMatrices[i][j] += matrixDos[i][j]
  return sumOfMatrices
       

print(addMatrices(matrix1, matrix2))