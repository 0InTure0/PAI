from email.mime import image
from tkinter import *
import time

window = Tk()
window.title("PAI")

Width = 960
Height = 640
canvas = Canvas(window, width=Width, height=Height, bg="black")
canvas.pack()
while True:
  for i in range(20):
    str_i = str(i)
    if(i < 10):
      str_i = "0"+str_i
    image_file = "PAI_ANI/blink/PAI_blink_000"+str_i+".png"
    PAI_img = PhotoImage(file=image_file)
    write_PAI = canvas.create_image(0, 0, anchor=NW, image=PAI_img)
    time.sleep(0.01)
    window.update()
  
  time.sleep(1)



window.mainloop()