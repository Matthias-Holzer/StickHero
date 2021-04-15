import numpy
import pyautogui
import pygetwindow as gw
from PIL import Image
import time
from pynput.mouse import Button, Controller

while True:
    #taking the screenshot
    pyautogui.screenshot('shot.png')

    #print(gw.getAllTitles())
    #get Window
    #print(gw.getActiveWindow())
    phone = 'scrcpy POCOPHONE F1'
    mac = 'Stick Hero Stick Hero'

    #get relative coordinates
    x, y, width, height = gw.getWindowGeometry(mac)
    print(gw.getWindowGeometry(mac))

    #croping the screenshot
    img = Image.open('shot.png')
    img = img.crop((x*2,y*2,(x+width)*2,(y+height)*2))
    img.save('croped.png')

    #processing
    shot = Image.open('croped.png')
    shot = numpy.array(shot, dtype=numpy.uint8)

    #defining the pixels
    pixels = [list(i[:3]) for i in shot[1300]]

    #print(pixels)
    transitions = []
    ignore = True
    black = True
    for i, pixel in enumerate(pixels):
        r = int(pixel[0])
        g = int(pixel[1])
        b = int(pixel[2])
        #if r > 240 and g < 30 and b <30:
        #    continue
        if r+g+b > 1:
            pixel[0] = 255
            pixel[1] = 255
            pixel[2] = 255

    for i, pixel in enumerate(pixels):
        r = int(pixel[0])
        g = int(pixel[1])
        b = int(pixel[2])
        if ignore and r+g+b > 1:
            #print(i,ignore)
            continue
        ignore = False
        #print('out of ignore',i,ignore)


        if black and r+g+b == 255*3:
            print('changed to color')
            black = not black
            transitions.append(i)
            continue

        if not black and r+g+b != 255*3:
            print('changed to black')
            black = not black
            transitions.append(i)
            continue

    print(pixels)
    print(len(pixels))

    print(transitions)
    c1, c2, c3 = transitions

    distance = (c2+c3)/2 - c1
    perfect = (distance/1000 -0.005) * 1.56
    print(distance)
    print(perfect)
    #reenforced learning

    print('bridge building')
    pyautogui.moveTo(x + width / 2, y + height / 2 +300)
    # pyautogui.leftClick((x+width)/2,(y+height)/2,0,distance)

    '''''
    pyautogui.mouseDown()
    time.sleep(perfect / 1000)
    pyautogui.mouseUp()
    '''''
    start = time.time()
    mouse = Controller()
    mouse.press(Button.left)
    time.sleep(perfect)
    mouse.release(Button.left)
    #pyautogui.dragTo(duration=perfect,button='left',_pause=False)
    end = time.time()
    print(end - start)

    #quit()
    time.sleep(4)
