def letterSummary(word):
    sumChars = {}
    for i in word:
        if i not in sumChars:
            sumChars[i] = 1
        else:
            sumChars[i] += 1
    print(sumChars)
        
    

if __name__ == "__main__":
    letterSummary('banana')