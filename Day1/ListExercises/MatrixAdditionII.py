matrix1 = [
    [1, 3],
    [2, 4],
    [1, 1]
]

matrix2 = [
    [5, 2],
    [1, 0],
    [1, 1]
]

def addMatrices(matrixUno, matrixDos):
  sumOfMatrices = matrixUno
  for i in range(0, len(sumOfMatrices)):
    for j in range(0, len(sumOfMatrices[i])):
      sumOfMatrices[i][j] += matrixDos[i][j]
  return sumOfMatrices
       

print(addMatrices(matrix1, matrix2))