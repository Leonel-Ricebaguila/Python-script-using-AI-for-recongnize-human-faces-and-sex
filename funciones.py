
def fpsModificator(pressedKey, fps):
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
    return fps

def whatIsLeosSexuality():
    print("GAYYYYY")
    return 120