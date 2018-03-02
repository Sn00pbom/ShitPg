import Image, ImageFont, ImageDraw

# ShowText = 'Python PIL'
#
# font = ImageFont.truetype('arialbd.ttf', 15) #load the font
# size = font.getsize(ShowText)  #calc the size of text in pixels
# image = Image.new('1', size, 1)  #create a b/w image
def mapBitToChar(im, col, row):
    if im.getpixel((col, row)):
        return ' '
    else:
        return '#'

def convertAndPrint(path):
    #path formatting like 'path'
    image = Image.open(path)
    image.convert('1')

    width, height = image.size


    # for rownum in range(height):
    #     # scan the bitmap:
    #     # print ' ' for black pixel and
    #     # print '#' for white one
    #     line = []
    #     for colnum in range(width):
    #         if image.getpixel((colnum, rownum)):
    #             line.append(' '),
    #         else:
    #             line.append('#'),
    #     print ''.join(line)


    for r in range(height):
        print ''.join([mapBitToChar(image, c, r) for c in range(width)])

