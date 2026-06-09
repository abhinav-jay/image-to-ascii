import argparse
from PIL import Image
from colorist import ColorRGB

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('filename')
args = parser.parse_args()
file = args.filename
imgwidth = int(input("enter the desired width of the image (in chars):"))

newimage2 = Image.open(file)
pix = newimage2.load()
print(" ")
dark = 0
light = 0
y = 0
n = newimage2.width/imgwidth

while y < newimage2.height / (n+0.00001):
    x = 0
    line = ""
    while x < newimage2.width / (n+0.00001):
        if (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3 < 50/brightness:
            line += "  "
        elif (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3 < 100/brightness:
            line += "||"
        elif (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3< 150/brightness:
            line += "@@"
        elif (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3 < 200/brightness:
            line += "##"
        else:
            line += "██"
        x += 1
    print(line)
    y += 1
