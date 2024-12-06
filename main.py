#Import libraries

import cv2 as computerVision
import numpy as numpy
import funciones

print("1")

# variables modificables
fps = 5
defaultWebCam = 0 # 0 communmente es la default
pressedKey = 255
videoCapturado = computerVision.VideoCapture(defaultWebCam) # captura objeto en videoEnVivo
face_cascade = computerVision.CascadeClassifier(computerVision.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:

    capturaExitosa, frame =  videoCapturado.read() # agarra un boolean (el exito) y un array (el frame)

    gray = computerVision.cvtColor(frame, computerVision.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        computerVision.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

    computerVision.imshow("LeoGayCam", frame) # actualiza el window
    pressedKey = computerVision.waitKey(1000//fps) & 0xFF
      
    # permite controlar el programa con teclas
    if (funciones.stopCapturing(pressedKey)): # sale del programa si se presiona q
        break
    fps = funciones.fpsModificator(pressedKey, fps) # suma con w y resta con s

    # checkeo de exito de la captura
    if capturaExitosa == False: #si no es exitosa, se rompe
        print("No se detecta camara bro, perdon :()")
        break

print("2")