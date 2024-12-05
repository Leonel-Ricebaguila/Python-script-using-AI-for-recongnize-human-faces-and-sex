#Import libraries

import time
import cv2 as computerVision
import numpy as numpy
import leoSexualityIdentifier

#variables modificables
fps = 10



videoEnVivo = computerVision.VideoCapture(0)

while True:
    ret, frame =  videoEnVivo.read()

    computerVision.imshow("LeoGayCam", frame)
    computerVision.waitKey(1000//fps)



print("1")
print("2")