from tkinter import *

class App():
    def __init__(self, master):

        self.frame = Frame(master, height =100 , width = 1000)
        self.frame.propagate(0)
        self.frame.pack()
        self.button = Button(self.frame, text = "QUI", fg = "RED", command = self.frame.quit, compound = CENTER)
        self.button.pack(fill=BOTH, expand = 1)
        self.button.config(bg = "red", command = self.callback, compound = RIGHT, font = "Algerian", fg = "yellow")


        self.hi_there = Button(self.frame, text = "HELLO",fg = "green", command = self.say_hi, compound = CENTER)
        self.hi_there.pack(fill=BOTH, expand = 1)

        self.butoon = Button(self.frame, text = "OK", command = self.callback,compound = CENTER)
        self.butoon.pack(fill = BOTH, expand = 1)

        self.view = Canvas(master,width = 200, height = 200)
        self.view.pack()
        self.view.create_line(0,0,200,100)
        self.view.create_line(0,100,200,0, fill = "red", dash = (44,44))
        self.view.create_rectangle(0,100,200,0, fill = "blue")

        self.other_line = self.view.create_line(0,0,50,50, fill = "orange")


    def say_hi(self):
        print("Hi there, everyone")
    def callback(self):
        print("click!")


root = Tk()
app = App(root)

root.mainloop()































