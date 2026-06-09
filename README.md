# Image/Video to ASCII converter
This converts images and video into ASCII.

## Note
`.png` format images don't work.
The colorful image thing may not be supported by every terminal, but the black and white image and the video should work on everything, make sure you terminal supports HEX ANSI codes.
The sync the sound and the video might be a bit off, the best height of the video for it to be good is around 200 characters.
If when executing the video, there is an error, you might need to unzoom your terminal. It is caused because there isn't enough space to draw the whole image inside the window.

## Dependencies
- colorist
- opencv
- argparse
- curses
- moviepy
- pillow

## Execution
To transform an image to a colorful ASCII, just execute
```bash
python image.py [filename]
```
To make a black and white ASCII (supported by every terminal), just execute
```bash
python imgbw.py [filename]
```
And to see a video in ASCII, just do
```bash
python video.py [filename]
```

Feel free to put issues and feature requests.
