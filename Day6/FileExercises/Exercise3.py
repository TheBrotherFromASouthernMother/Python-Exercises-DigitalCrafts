import sys
sys.path.append("../")
from DictionaryExercises.wordSummary import wordSummary
from DictionaryExercises.letterSummary import letterSummary

fileName = str(input("Please write the name of the file you would like to open: "))
file_handle = open(fileName, "r")
contents = file_handle.read()
file_handle.close()

wordSummary(contents)
letterSummary(contents)