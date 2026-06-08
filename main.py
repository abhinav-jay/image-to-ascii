from PIL import Image
brightness = float(input("enter brightness level, (1 is default):"))
newimage2 = Image.open("/home/abhinav/Documents/achachanachamma.png")
pix = newimage2.load()
print(newimage2.size)
print(" ")
dark = 0
light = 0
y = 0
n = newimage2.width/160

while y < newimage2.height / (n+0.1):
    x = 0
    line = "                                                            "
    while x < newimage2.width / (n+0.1):
        if (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3 < 50/brightness:
            line += "  "
            x += 1
        elif (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3 < 100/brightness:
            line += "||"
            x += 1
        elif (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3< 150/brightness:
            line += "@@"
            x += 1
        elif (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3 < 200/brightness:
            line += "##"
            x += 1
        else:
            line += "██"
            x += 1
    print(line)
    y += 1
