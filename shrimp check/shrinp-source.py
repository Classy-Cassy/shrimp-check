from tkinter import *
from PIL import ImageTk, Image
import time
import random


# defining the window
def window():
    global root
    global my_label
    global button_exit
    global img
    root = Tk()
    root.title('Shrimp Check')
    img = ImageTk.PhotoImage(Image.open(r'Shrimp jpeg path')) #replace here
    my_label = Label(image=img)
    button_exit = Button(root, text= "Terminate Program", command= exit)

def jumpscare():
    root.iconbitmap(r'shrimp ico path') # Replace here
    my_label.pack()
    button_exit.pack()
    root.bell()
    root.mainloop()



while True:
    time.sleep(random.randint(5,10))
    window()
    jumpscare()