arr = [4, 5, 6]
arr2 = [2, 1, 3]

def multiplyVectors(list, list2):
    multipliedList = []
    for i in range(0, len(list)):
        print(i)
        multipliedList.append(list[i] * list2[i])    
    return multipliedList

print(multiplyVectors(arr, arr2))