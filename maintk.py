from tkinter import *

class App():
    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()
        self.button = Button(self.frame, text = "QUI", fg = "RED", state = DISABLED)
        self.button.pack(side = LEFT)

        self.hi_there = Button(self.frame, text = "HELLO",fg = "green", command = self.say_hi)
        self.hi_there.pack(side= LEFT)

        butoon = Button(text = "OK", command = self.callback)
        butoon.pack(side = RIGHT)

    def say_hi(self):
        print("Hi there, everyone")
    def callback(self):
        print("click!")

root = Tk()
app = App(root)

root.mainloop()































