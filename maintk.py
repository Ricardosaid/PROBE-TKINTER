from tkinter import *

class App():
    def __init__(self, master):

        self.frame = Frame(master, height =100 , width = 100)
        self.frame.propagate(0)
        self.frame.pack()
        self.button = Button(self.frame, text = "QUI", fg = "RED", command = self.frame.quit)
        self.button.pack(fill=BOTH, expand = 1)
        self.button.pack(side = RIGHT)

        self.hi_there = Button(self.frame, text = "HELLO",fg = "green", command = self.say_hi)
        self.hi_there.pack(fill=BOTH, expand = 1)
        self.hi_there.pack(side = LEFT)

        self.butoon = Button(self.frame, text = "OK", command = self.callback)
        self.butoon.pack(fill = BOTH, expand = 1)
        self.butoon.pack(side = TOP)
        #self.butoon.pack(side = RIGHT)

    def say_hi(self):
        print("Hi there, everyone")
    def callback(self):
        print("click!")


root = Tk()
app = App(root)

root.mainloop()































