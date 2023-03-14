from tkinter import *
from PIL import ImageTk, Image
import time
import random
import os
from sys import exit



# defining the window
def window():
    global root
    global my_label
    global button_exit
    global img
    root = Tk()
    root.attributes("-topmost", True)
    root.title('Shrimp Check')
    img = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\shrimp-gun.png')) 
    my_label = Label(image=img)
    button_exit = Button(root, text= "Terminate Program", command= exit)

#Show the window
def jumpscare():
    root.iconbitmap(os.getcwd()+'\\shrimpicon.ico') 
    my_label.pack()
    button_exit.pack()
    root.bell()
    root.mainloop()



while True:
    time.sleep(random.randint(15,30) * 60) #Change the random time interval here
    window()
    jumpscare()