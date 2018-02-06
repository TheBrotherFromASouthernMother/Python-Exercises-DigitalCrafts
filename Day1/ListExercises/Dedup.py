arr = [1,2,3,4,5,1,2,3,4,5]
arr2 = ['s', 't', 'r', 'i', 'n', 'g', 's', 't']
arr3 = [2,5,2,5,7,7, 9, 8, 9, 2, 2, 2]

def removeDuplicates(list):
    ListWithNoRepeats = []
    for i in list:
        if i not in ListWithNoRepeats:
            ListWithNoRepeats.append(i)
    return ListWithNoRepeats
        



print(removeDuplicates(arr3))