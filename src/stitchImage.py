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
    html = "<html><head><title>Breaking Bad-ify</title></head><body>"
    for lineTranslation in fileTranslation:
        for wordTranslation in lineTranslation:
            filePath = "out/" + "".join(wordTranslation) + ".png"
            createWordImage(wordTranslation).save(filePath, "PNG")
            html = html + "<img src='" + filePath + "'>"
            html = html + "<img src='src/space.png'>"
    html = html + "</body></html>"
    file = open("index.html","w")
    file.write(html)
    file.close()         
