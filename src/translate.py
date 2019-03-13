from sys import argv
import csv

def getSymbolList():

    symbolList = []

    with open('res/elementList.csv', mode='r') as elementFile:
        reader = csv.reader(elementFile)
        symbolList = [row[1] for row in reader]
    
    return symbolList

def getWordArray(textString):
    
    wordList = []
    newWord = True

    for character in textString:
        if newWord:
            if character.isalpha():
                wordList += [character]
                newWord = False
        else:
            if character.isalpha():
                wordList[-1] += character
            else:
                newWord = True
    
    return wordList

def translateWord(word):
    
    symbolList = getSymbolList()
    translation = []

    # TODO: Code algorithm for word translation

    return translation

fileNames = argv[1:]

for fileName in fileNames:
    lines = open(fileName).readlines()
    
    for line in lines:
        words = getWordArray(line)

