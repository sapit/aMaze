from PIL import Image

width = None
height = None

def getImageAsList(fname):
    global width
    global height
    pix = getImageData(fname)
    grid = []
    for h in xrange(height):
        temp = []
        for w in xrange(width):
            temp += [ 1 if pix[w,h] == (255, 255, 255) else 0 ]
        grid += [temp]
    return grid

def getImageAsString(fname):
    grid = getImageAsList(fname)
    result = ""
    return result.join(str(x) for l in grid for x in l)

def getImageData(fname):
    img = Image.open(fname)
    pix = img.load()
    global width
    global height
    width, height = img.size
    return pix

def getImageWidth(fname):
    global width
    if not width:
        getImageData(fname)
    return width

def getImageHeight(fname):
    global height
    if not height:
        getImageData(fname)
    return height
