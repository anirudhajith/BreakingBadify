import csv

def getSymbolSet():
    """ 
    Retrieves set of symbols of chemical elements from res/elementList.csv.
  
    Returns: 
    set: set of symbols of chemical elements
  
    """

    symbolSet = set()

    with open('res/elementList.csv', mode='r') as elementFile:
        reader = csv.reader(elementFile)
        symbolSet = {row[1] for row in reader}
    
    return symbolSet

def getWordArray(textString):
    """ 
    Returns a list of words after processing input string.
  
    Parameters: 
    textString (string): textString to be split into words 
  
    Returns: 
    list: list of words obtained by splitting textString 
  
    """
    
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
    
    wordList = [word.lower() for word in wordList]

    return wordList

def translateWord(word):
    """ 
    Converts word into its chemical element translation.
  
    Parameters: 
    word (string): Word which has to be translated

    Returns: 
    list: containing the individual elements which make up the word 
  
    """

    symbolSet = getSymbolSet()
    translation = []

    if len(word) > 1:

        if word[0:2].title() in symbolSet:
            translation.append(word[0:2].title())
        else:
            if word[0].title() in symbolSet:
                translation.append(word[0].title())
            else:
                translation.append(word[0])
            
            if word[1].title() in symbolSet:
                translation.append(word[1].title())
            else:
                translation.append(word[1])

        for i in range(2, len(word)):
            if word[i-1 : i+1].title() in symbolSet:
                if len(translation[-1]) == 1:
                    translation.pop()
                    translation.append(word[i-1 : i+1].title())
                else:
                    if word[i].title() in symbolSet:
                        translation.append(word[i].title())
                    else:
                        translation.append(word[i])      
            elif word[i].title() in symbolSet:
                translation.append(word[i].title())
            else:
                translation.append(word[i])
    else:
        if word in symbolSet:
            translation.append(word.title())
        else:
            translation.append(word)
    
    return translation

def translateFile(fileName):
    """ 
    Returns a nested list representing the chemical element translation of a file.
  
    Parameters: 
    fileName (string): Name of file to be read 
  
    Returns: 
    list: A nested list representing the chemical element translation of a file
  
    """

    lines = open(fileName).readlines()
    
    fileTranslation = []

    for line in lines:
        words = getWordArray(line)
        lineTranslation = [translateWord(word) for word in words]
        fileTranslation.append(lineTranslation)

    return fileTranslation
