arr = [1, -2, 3, 4, -5, 6, 3.7, 0.8, -0.9, -10]
arr1 = [19, 5, 42, 70, 55, 2, 12, 37, 84]

def FindPositiveNumbers(list):
    positiveNumbers = []
    for i in list:
        if i > 0:
            positiveNumbers.append(i)
    return positiveNumbers


print(FindPositiveNumbers(arr1))