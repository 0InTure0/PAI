from email.mime import image
from tkinter import *
import time

window = Tk()
window.title("PAI")

Width = 480
Height = 320
canvas = Canvas(window, width=Width, height=Height, bg="black")
canvas.pack()

#두리번 거리기
def left_right():
    a = 0
    while(a <= 20):
        canvas.move(black_eye1, 2, 0)
        canvas.move(black_eye2, 2, 0)
        canvas.move(white_eye1, 1, 0)
        canvas.move(white_eye2, 1, 0)
        canvas.move(eyeblow_right, 1, -0.5)
        time.sleep(0.01)
        window.update()
        a = a + 1
    
    a = 0
    while(a <= 20):
        canvas.move(black_eye1, -2, 0)
        canvas.move(black_eye2, -2, 0)
        canvas.move(white_eye1, -1, 0)
        canvas.move(white_eye2, -1, 0)
        canvas.move(eyeblow_right, -1, 0.5)
        time.sleep(0.01)
        window.update()
        a = a + 1

    a = 0
    while(a <= 20):
        canvas.move(black_eye1, -2, 0)
        canvas.move(black_eye2, -2, 0)
        canvas.move(white_eye1, -1, 0)
        canvas.move(white_eye2, -1, 0)
        canvas.move(eyeblow_left, -1, -0.5)
        time.sleep(0.01)
        window.update()
        a = a + 1

    a = 0
    while(a <= 20):
        canvas.move(black_eye1, 2, 0)
        canvas.move(black_eye2, 2, 0)
        canvas.move(white_eye1, 1, 0)
        canvas.move(white_eye2, 1, 0)
        canvas.move(eyeblow_left, 1, 0.5)
        time.sleep(0.01)
        window.update()
        a = a + 1

def move():
    a = 0
    b = 0
    while(a <= 55):
        black_rec1 = canvas.create_rectangle(10, 90, 470, 100+b, fill="black")
        time.sleep(0.01)
        window.update()
        a = a + 1
        b = b + 1
    


#눈 그리기

white_eyes_img = PhotoImage(file='design/white_eyes.png')
black_eyes_img = PhotoImage(file='design/black_eyes.png')
white_eye1 = canvas.create_image(85, 100, anchor=NW, image=white_eyes_img)
white_eye2 = canvas.create_image(285, 100, anchor=NW, image=white_eyes_img)
black_eye1 = canvas.create_image(110, 125, anchor=NW, image=black_eyes_img)
black_eye2 = canvas.create_image(310, 125, anchor=NW, image=black_eyes_img)

#눈썹 불러오기
eyeblow_left_img = PhotoImage(file='design/eyeblow_left.png')
eyeblow_right_img = PhotoImage(file='design/eyeblow_right.png')
eyeblow_left = canvas.create_image(75,45, anchor=NW, image=eyeblow_left_img)
eyeblow_right = canvas.create_image(285,45, anchor=NW, image=eyeblow_right_img)

#눈 감기

move()

while(1):
    left_right()

window.mainloop()