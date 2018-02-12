def wordSummary(phrase):
    wordSum = {}
    wordList = phrase.split(' ')
    for word in wordList:
        if word not in wordSum:
            wordSum[word] = 1
        else:
            wordSum[word] += 1
    print(wordSum)

wordSummary("I came I saw I conquered.")
