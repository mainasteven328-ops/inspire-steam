
from tkinter import *

def faah():
    print("nigga get outta here")


root = Tk()
root.geometry("400x400")

frame_one = Frame(root)
frame_one.pack()

button_one= Button(frame_one, text= "whats good lil homie", command=faah)
button_one.pack()

root.mainloop()

