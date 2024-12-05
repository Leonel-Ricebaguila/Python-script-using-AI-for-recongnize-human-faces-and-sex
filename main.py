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
pressedKey = 'a'

videoEnVivo = computerVision.VideoCapture(defaultWebCam) # captura objeto en videoEnVivo

while True:

    capturaExitosa, frame =  videoEnVivo.read() # agarra un boolean (el exito) y un array (el frame)
    computerVision.imshow("LeoGayCam", frame) # actualiza el window
    pressedKey = computerVision.waitKey(1000//fps)
    
    # permite controlar el programa con teclas
    if pressedKey == ord('q'): # sale del programa si se presiona q
        print("STAWWWWP")
        break
    
    if pressedKey == ord('w'): # suma un fps al programa
        if fps == 240:
            print("cant go above 240 buddie >:V")
        else:
            fps = (fps+1)
            print(f"fps = {fps}")
    elif pressedKey == ord('s'): # resta un fps al programa
        if fps == 1:
            print("cant go below 0 buddie >:V")
        else:
            fps = (fps-1)
            print(f"fps = {fps}")    

    #fps = funciones.fpsModificator(pressedKey, fps) #### QUIEN SABE PORQUE NO FUNCIONA ####

    # checkeo de exito de la captura
    if capturaExitosa == False: #si no es exitosa, se rompe
        print("Se rompio bro, perdon :()")
        break

print("2")