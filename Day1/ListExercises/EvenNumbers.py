arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr1 = [19, 5, 42, 70, 55, 2, 12, 37, 84]

def FindEvenNumbers(list):
    for i in list:
        if i % 2 == 0:
            print(i)


FindEvenNumbers(arr)