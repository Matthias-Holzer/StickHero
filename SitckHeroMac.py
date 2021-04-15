import numpy
import pyautogui
import pygetwindow as gw
from PIL import Image
import time
from pynput.mouse import Button, Controller

lastDistance = 0

while True:
    #taking the screenshot
    pyautogui.screenshot('imgs/shot.png')

    #print(gw.getAllTitles())
    #get Window
    #print(gw.getActiveWindow())
    #phone = 'scrcpy POCOPHONE F1'
    mac = 'Stick Hero Stick Hero'

    #get relative coordinates
    x, y, width, height = gw.getWindowGeometry(mac)
    print(gw.getWindowGeometry(mac))

    #croping the screenshot
    img = Image.open('imgs/shot.png')
    img = img.crop((x*2,y*2,(x+width)*2,(y+height)*2))
    img.save('imgs/croped.png')

    #
    xOver1 = 700
    yOver1 = 400
    xOver2 = 800
    yOver2 = 420

    over = Image.open('imgs/croped.png')
    over = over.crop((700,400,800,420))
    over.save('imgs/over.png')
    over = numpy.array(over, dtype=numpy.uint8)
    pixelsOver = [list(i[:3]) for i in over[0]]

    gameOver = True
    for i, pixel in enumerate(pixelsOver):
        r = int(pixel[0])
        g = int(pixel[1])
        b = int(pixel[2])
        if r != 255 or g != 255 or b != 255:
            gameOver = False
            print("not white",i)
            break
    if gameOver:
        print("game Over!!!")
        print('distance: ',lastDistance)
        pyautogui.leftClick((x) / 2 + 900, (y + 1190) / 2)
        time.sleep(0.5)
        continue

    #processing
    shot = Image.open('imgs/croped.png')
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

    #print(pixels)
    #print(len(pixels))
    #print(transitions)

    try:
        c1, c2, c3 = transitions

        distance = (c2+c3)/2 - c1
        lastDistance = distance
        perfect = (distance/1000 - 0.002) * 0.90
        print('distance: ',distance)
        print('perfect: ',perfect)
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

        if distance > 300:
            time.sleep(0.9)
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep((perfect - 0.1) * 1.2)
            mouse.press(Button.left)
            mouse.release(Button.left)

        file = open('data/executingDifference.txt',"a")
        save = str(str((end - start) -perfect)+"\n")
        print(save)
        file.write(save)
        file.close()
    except NotImplementedError as e:
        print("something went wrong!!!", e)

    #quit()
    time.sleep(2.7)
