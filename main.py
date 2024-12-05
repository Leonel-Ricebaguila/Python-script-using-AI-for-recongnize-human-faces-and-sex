#Import libraries

import time
import cv2 as computerVision
import numpy as numpy
import leoSexualityIdentifier

#variables modificables
fps = 5
defaultWebCam = 0 # 0 communmente es la default
exitKey = "q"

videoEnVivo = computerVision.VideoCapture(defaultWebCam)

capturaExitosa, frame =  videoEnVivo.read()

while capturaExitosa:

    capturaExitosa, frame =  videoEnVivo.read()
    computerVision.imshow("LeoGayCam", frame) #actualiza el window
    computerVision.waitKey(1000//fps)  #hace delay de 1000 milisegundos entre los fps

    if capturaExitosa == False:
        print("Se rompio bro, perdon :()")
        break



print("1")
print("2")