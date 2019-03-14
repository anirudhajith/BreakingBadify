import sys
import src.translate as translate
import src.stitchImage as img

files = sys.argv[1:]

for file in files:
    fileTranslation = translate.translateFile(file)
    print(fileTranslation)
    img.createFileImage(fileTranslation)