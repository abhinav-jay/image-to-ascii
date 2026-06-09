import argparse
import moviepy
import pygame
import time
from PIL import Image
from colorist import ColorRGB
import cv2
import curses
from curses import wrapper

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('filename')
args = parser.parse_args()
file = args.filename
videoheight = int(input("enter the desired height of the video (in chars): "))

content = moviepy.VideoFileClip(file)
content.audio.write_audiofile("audio.mp3")

brightness = float(input("enter brightness level:"))

def main(stdscr):

    stdscr.getch()

    stdscr.clear()

    video = cv2.VideoCapture(file)
    frame = 0
    nb_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    framediff = fps/3.56

    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play()

    # import pdb; pdb.set_trace()
    while frame < nb_frames:
    
        video.set(1, frame)
        success, img = video.read()
        cv2.imwrite("image.jpg", img)
        newimage2 = Image.open("image.jpg")
        
        pix = newimage2.load()
        print(" ")
        dark = 0
        light = 0
        y = 0
        n = newimage2.height/videoheight

        stdscr.getch()
        while y < newimage2.height / (n+0.1):
            x = 0
            while x < newimage2.width / (n+0.1):

                if (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3 < 50/brightness:
                    stdscr.addstr(y,2*x,"  ")
                elif (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3 < 100/brightness:
                    stdscr.addstr(y,2*x,"||")
                elif (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3 < 150/brightness:
                    stdscr.addstr(y,2*x,"@@")
                elif (pix[n*x,n*y][0] + pix[n*x,n*y][1] + pix[n*x,n*y][2])/3 < 200/brightness:
                    stdscr.addstr(y,2*x,"##")
                else:
                    stdscr.addstr(y,2*x,"██")
                x += 1
            y += 1

        frame += framediff
        # time.sleep(0.15)
    stdscr.refresh()
    

wrapper(main)
