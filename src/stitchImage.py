from PIL import Image, ImageFont, ImageDraw

sideLength, _ = Image.open('res/tiles/H.png').size

def createWordImage(wordTranslation):
    width = sideLength * len(wordTranslation)
    height = sideLength

    wordImage = Image.new('RGB', (width, height))
    textDrawer = ImageDraw.Draw(wordImage)
    font = ImageFont.truetype("res/Roboto.ttf", int(sideLength * 0.3))
    xOffset = 0

    for element in wordTranslation:
        if element.istitle():
            elementImage = Image.open("res/tiles/" + element + ".png")
            wordImage.paste(elementImage, (xOffset, 0, xOffset + sideLength, height))
        else:
            textDrawer.text((xOffset + 0.4 * sideLength, 0.25 * sideLength), element, font = font)
        xOffset += sideLength
    
    return wordImage


def createFileImage(fileTranslation):
    for lineTranslation in fileTranslation:
        for wordTranslation in lineTranslation:
            createWordImage(wordTranslation).save("out/" + "".join(wordTranslation) + ".png", "PNG")
