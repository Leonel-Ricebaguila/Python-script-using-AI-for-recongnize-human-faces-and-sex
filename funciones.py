

# permite controlar el programa con teclas
def stopCapturing(pressedKey):
    if pressedKey == ord('q'): # sale del programa si se presiona q
        print("STAWWWWP")
        return True
    return False

def fpsModificator(pressedKey, fps):
    if pressedKey == ord('w'): # suma un fps al programa
        if fps == 240:
            print("cant go above 240 buddie >:V")
        else:
            print(f"fps = {fps}")
            return (fps+1)
    elif pressedKey == ord('s'): # resta un fps al programa
        if fps == 1:
            print("cant go below 0 buddie >:V")
        else:
            print(f"fps = {fps}")
            return (fps-1)
    return fps

def whatIsLeosSexuality():
    print("GAYYYYY")
    return 120