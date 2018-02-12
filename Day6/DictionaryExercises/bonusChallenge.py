def letterSummary(word):
    sumChars = {}
    for i in word:
        if i not in sumChars:
            sumChars[i] = 1
        else:
            sumChars[i] += 1
    print(sumChars)
    tally = list(sumChars.keys())
    firstPlace = tally[0]
    for j in tally:
        if sumChars[j] > sumChars[firstPlace]:
            firstPlace = j

    print('Top Result \"{}\" count: {}'.format(firstPlace,  sumChars[firstPlace]))
    return sumChars
        
    

if __name__ == "__main__":
    letterSummary('banana')