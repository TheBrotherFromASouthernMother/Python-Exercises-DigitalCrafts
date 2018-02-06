matrix1 = [
    [2, -2],
    [5, 3]
]

matrix2 = [
    [-1, 4],
    [7, -6]
]

def addMatrices(matrixUno, matrixDos):
  productOfMatrices = [
      [],
      []
  ]
  for i in range(0, len(matrixUno)):
      #loop through columns
      for j in range(0, len(matrixUno)):
          #loop through rows of both 
          print(j)
      for k in range(0, len(matrixUno)):
          #loop through columns of second matrix
          productOfMatrices[i].append(matrixUno[i][k] * matrixDos[i][j])
          
  return productOfMatrices


       

print(addMatrices(matrix1, matrix2))