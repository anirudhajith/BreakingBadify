import csv

def getSymbolSet():

    symbolSet = set()

    with open('res/elementList.csv', mode='r') as elementFile:
        reader = csv.reader(elementFile)
        symbolSet = {row[1] for row in reader}
    
    return symbolSet

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

    word = word.lower()
    symbolSet = getSymbolSet()
    translation = []

    if word[0:2] in symbolSet:
        translation.append(word[0,2].title())
    else:
        if word[0] in symbolSet:
            translation.append(word[0].title())
        else:
            translation.append(word[0])
        
        if word[1] in symbolSet:
            translation.append(word[1].title())
        else:
            translation.append(word[1])

    for i in range(2, len(word)):
        if word[i-1 : i+1] in symbolSet:
            if len(translation[-1]) == 1:
                translation.pop()
                translation.append(word[i-1 : i+1].title())
        else if word[i] in symbolSet:
            translation.append(word[i].title())
        else:
            translation.append(word[i])
    
    return translation

def translateFile(fileName):
    lines = open(fileName).readlines()
    
    fileTranslation = []

    for line in lines:
        words = getWordArray(line)
        lineTranslation = [translateWord(word) for word in words]
        fileTranslation.append(lineTranslation)
    
    return lineTranslation
