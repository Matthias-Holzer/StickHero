import numpy
import pyautogui
import pygetwindow
from PIL import Image
import time

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

while True:
    #taking the screenshot
    pyautogui.screenshot('shot.png')

    #get relative coordinates
    phone = 'scrcpy POCOPHONE F1'
    x, y, width, height = pygetwindow.getWindowGeometry(phone)
    print(pygetwindow.getWindowGeometry(phone))

    #croping the screenshot
    img = Image.open('shot.png')
    img = img.crop((x*2,y*2,(x+width)*2,(y+height)*2))
    img.save('croped.png')

    #processing
    shot = Image.open('croped.png')
    shot = numpy.array(shot, dtype=numpy.uint8)

    #defining the pixels
    pixels = [list(i[:3]) for i in shot[1069]]

    #defining the colours
    red = list[
        [245,27,26],
        [188,27,26],
        [54,0,0],
        [112,14,12],
        [245,27,25]
    ]

    #transitions
    transitions = []
    redTransitions = []
    ignore= True
    black = True
    
    redPositions = []
    
    for i, pixel in enumerate(pixels):

        r, g, b = [int(i) for i in pixel]
        print(r, g, b)
        if ignore and (r + g + b) != 1:
            continue

        ignore = False

        if r==245 and g==27 and b == 26:
            redPositions.append(i)
            continue

        if black and (r + g + b) > 1:
            black = not black
            transitions.append(i)
            continue

        if not black and (r + g + b) == 1:
            black = not black
            transitions.append(i)
            continue


    print(transitions)
    start,target1, target2 = transitions

    gap = target1 - start
    target = target2 - target1
    distance = (gap + target / 2)

    middle = findMiddle(redPositions)
    perfect = middle - start

    print(f'transition points: {transitions}, distance: {distance}')


    print('done')

    time.sleep(2.7)

