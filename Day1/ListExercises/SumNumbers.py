arr = [1,2,3,4,5,6,7,8,9,10]

def makeSumOfList(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(makeSumOfList(arr))