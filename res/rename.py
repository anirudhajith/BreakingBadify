import os
import csv

symbolDict = {}
here = os.getcwd() + "/tiles/"

with open('elementList.csv', mode='r') as elementFile:
    reader = csv.reader(elementFile)
    symbolDict = {row[2] : row[1] for row in reader}

for filename in os.listdir("tiles"):
    if len(filename.split('-')) == 3:
        element = filename.split('-')[1]
        os.renames(here + filename, here + symbolDict[element] + ".png")
