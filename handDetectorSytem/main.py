import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import screeninfo
import sys

def main(path, threshold = 400, right=[0, 0, 0, 0, 1], left = [1, 0, 0, 0, 0], showPointer=[0, 1, 1, 0, 0], draw=[0, 1, 0, 0, 0], erase=[0, 1, 1, 1, 0], changeColor=[0, 1, 1, 1, 1]):
    os.system('cd /')

    width, height = 1280, 720
    folderPath = path

    # Camera setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # Get the list of presentation images
    pathImages = sorted(os.listdir(folderPath), key=len)

    # Variables
    imgNumber = 0
    hs, ws = 120, 213
    gestureThreshold = threshold
    buttonPressed = False
    buttonCounter = 0
    buttonDelay = 20
    annotations = []
    annotationNumber = -1
    annotationStart = False
    pointerColor = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    colorNumber = 0
    colorList = []
    verif = False
    # Hand Detector 
    detector = HandDetector(detectionCon=0.8, maxHands=1)



    # get the size of the screen
    screen = screeninfo.get_monitors()[0]
    scrren_width, screen_height = screen.width, screen.height

    while True :
        # Import images
        success, img = cap.read()
        img = cv2.flip(img, 1)

        pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
        imgCurrent = cv2.imread(pathFullImage)
        imgCurrent = cv2.resize(imgCurrent, (scrren_width, screen_height))
        

        hands, img = detector.findHands(img, flipType=False)
        cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)

        if hands and buttonPressed is False: 
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            fingers[0] = int(not bool(fingers[0]))
            cx, cy = hand['center']
            lmList = hand['lmList']

            # Contrain values for easier drawing
            indexFinger = lmList[8][0], lmList[8][1]
            xVal = int(np.interp(lmList[8][0], [width//2-30, w-30], [0, width]))
            yVal = int(np.interp(lmList[8][1], [200, height-200], [0, height]))
            indexFinger = xVal, yVal

            # If the gesture is in the height of the face
            if cy <= gestureThreshold:

                # Gesture 1 - Left
                if fingers == left:
                    print('left')
                    if imgNumber > 0:
                        buttonPressed = True
                        imgNumber -= 1
                        annotations = []
                        annotationNumber = -1
                        annotationStart = False
                        colorNumber = 0
                        colorList = []
                        verif = False

                # Gesture 2 - Right
                if fingers == right:
                    annotationStart = False
                    
                    if imgNumber < len(pathImages)-1:
                        buttonPressed = True
                        imgNumber += 1
                        annotations = []
                        annotationNumber = -1
                        colorNumber = 0
                        colorList = []
                        verif = False
                
                # Gesture 6 - Change pointer color
                if fingers == changeColor:
                    buttonPressed = True
                    colorNumber = (colorNumber+1) % len(pointerColor)

                # Gesture 5 - erase
                if fingers == erase:
                    if annotations and annotationNumber >= 0 :
                        annotations.pop(-1)
                        annotationNumber -= 1
                        buttonPressed = True
                        colorList.pop(-1)
                        

            # Gesture 3 - Show Pointer
            if fingers == showPointer:
                print(indexFinger)
                cv2.circle(imgCurrent, indexFinger, 12, pointerColor[colorNumber], cv2.FILLED)

            # Gesture 4 - Draw Pointer
            if fingers == draw:
                if annotationStart is False :
                    annotationStart = True
                    annotationNumber += 1
                    annotations.append([])
                    colorList.append(colorNumber)
                cv2.circle(imgCurrent, indexFinger, 12, pointerColor[colorNumber], cv2.FILLED)
                annotations[annotationNumber].append(indexFinger)
                verif = True
            else:
                annotationStart = False


        else:
            annotationStart = False



        # Button Pressed iterations
        if buttonPressed:
            buttonCounter += 1
            if buttonCounter > buttonDelay:
                buttonCounter = 0
                buttonPressed = False

        if verif:
            for i in range(len(annotations)):
                for j in range(1, len(annotations[i])):
                    cv2.line(imgCurrent, annotations[i][j-1], annotations[i][j], pointerColor[colorList[i]], 12)

        # Adding webcam image on the slides
        imgSmall = cv2.resize(img, (ws, hs))
        h, w, c = imgCurrent.shape
        imgCurrent[0:hs, w-ws:w] = imgSmall

        cv2.imshow('Slides', imgCurrent)



        key = cv2.waitKey(1)
        if key == ord('q'):
            break

