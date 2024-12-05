#Import libraries

import time
import cv2 as computerVision
import numpy as numpy
import keyboard
import funciones

print("1")

# variables modificables
fps = 5
defaultWebCam = 0 # 0 communmente es la default
pressedKey = 255
videoCapturado = computerVision.VideoCapture(defaultWebCam) # captura objeto en videoEnVivo

while True:

    capturaExitosa, frame =  videoCapturado.read() # agarra un boolean (el exito) y un array (el frame)
    computerVision.imshow("LeoGayCam", frame) # actualiza el window
    pressedKey = computerVision.waitKey(1000//fps) & 0xFF
    # permite controlar el programa con teclas
    
    if (funciones.stopCapturing(pressedKey)) or 1==1: # sale del programa si se presiona q
        break

    fps = funciones.fpsModificator(pressedKey, fps) 

    # checkeo de exito de la captura
    if capturaExitosa == False: #si no es exitosa, se rompe
        print("Se rompio bro, perdon :()")
        break

print("2")