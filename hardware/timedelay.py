import time

sleeptm = time.time() + 3
while True:
    if(time.time() > sleeptm):
        print("hellow")
        sleeptm = time.time() + 3