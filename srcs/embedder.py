from fontTools import ttLib
import base64
import sys
import os

def fileToBase64(filePath):
    with open(filePath, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

def stringToByte(string):
    return bytes(string, encoding='utf-8')

if '-i' not in sys.argv or '-m' not in sys.argv:
    print('The arguements -i and -m is required!')
    sys.exit()
fontPath = sys.argv[sys.argv.index('-i') + 1]
fontFileName = os.path.basename(fontPath)
embededPath = sys.argv[sys.argv.index('-m') + 1]
embeddingFileName = os.path.basename(embededPath)
if '-o' in sys.argv:
    exportPath = sys.argv[sys.argv.index('-o') + 1]
else:
    exportPath = sys.argv[sys.argv.index('-i') + 1]
exportFileName =  os.path.basename(exportPath)
if '-tag' in sys.argv:
    tag = sys.argv[sys.argv.index('-tag') + 1]
    if len(tag) > 4:
        print('Custom tag must specified 4 characters only.')
        sys.exit()
else:
    tag = 'mbdd'
base64File = fileToBase64(embededPath)
byteData = stringToByte(base64File)
font = ttLib.TTFont(fontPath)
if 'meta' in font:
    if tag in font['meta'].data:
        print(fontFileName + ' already embedded.')
        sys.exit()
    else:
        font['meta'].data[tag] = byteData
else:
    metaTable = ttLib.newTable('meta')
    metaTable.data = {tag : byteData}
    font['meta'] = metaTable
font.save(exportPath)
print('Embeded the ' + embeddingFileName + ' to ' + exportFileName)