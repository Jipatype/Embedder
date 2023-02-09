from fontTools import ttLib
import base64
import sys
import os

def base64ToFile(base64Str, filePath):
    with open(filePath, "wb") as file:
        file.write(base64.b64decode(base64Str.encode("utf-8")))

def byteToString(byteObj):
    return byteObj.decode(encoding='utf-8')

if '-i' not in sys.argv or '-o' not in sys.argv:
    print('The arguements -i and -o is required!')
    sys.exit()
if '-tag' in sys.argv:
    tag = sys.argv[sys.argv.index('-tag') + 1]
    if len(tag) != 4:
        print('Custom tag must specified 4 characters only.')
        sys.exit()
else:
    tag = 'mbdd'
fontPath = sys.argv[sys.argv.index('-i') + 1]
fontFileName = os.path.basename(fontPath)
exportPath = sys.argv[sys.argv.index('-o') + 1]
fileName = os.path.basename(exportPath)
font = ttLib.TTFont(fontPath)
if 'meta' in font:
    if tag in font['meta'].data:
        base64String = byteToString(font['meta'].data[tag])
        base64ToFile(base64String, exportPath)
        print('Extracted the ' + fontFileName + ' to ' + fileName)
    else:
        print('There is nothing embedded in the ' + fontFileName)
else:
    print('There is nothing embedded in the ' + fontFileName)