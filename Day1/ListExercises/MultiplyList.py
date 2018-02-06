arr = [1, 2, 3, 4, 5, 6, 3, 8, 9, 10]
arr1 = [19, 5, 42, 70, 55, 2, 12, 37, 84]

def MultiplyList(list, factor):
    multipliedList = []
    for i in list:
        multipliedList.append(i * factor)
    return multipliedList


print(MultiplyList(arr, 2))