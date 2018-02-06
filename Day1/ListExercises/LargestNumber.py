arr = [1,2,3,4,5,6,7,8,9,10]
arr1 = [19, 5, 42, 70, 55, 2, 12, 37, 84]

def FindLargestNumber(list):
    largestNum = list[0]
    for i in list:
        if i > largestNum:
            largestNum = i
    return largestNum

print(FindLargestNumber(arr))

print(FindLargestNumber(arr1))