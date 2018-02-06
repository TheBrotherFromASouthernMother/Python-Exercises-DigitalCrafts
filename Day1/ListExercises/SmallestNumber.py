arr = [1,2,3,4,5,6,7,8,9,10]
arr1 = [19, 5, 42, 70, 55, 8, 12, 37, 84]

def FindSmallestNumber(list):
    smallestNum = list[0]
    for i in list:
        if i < smallestNum:
            smallestNum = i
    return smallestNum

print(FindSmallestNumber(arr))

print(FindSmallestNumber(arr1))