'''
Created on Nov 1, 2014

@author: chris
'''
from Tkinter import *

class App:
    
    def __init__(self, root):
        
        frame = Frame(root)
        frame.pack()
         
        self.btnQuit = Button (
            frame, text = "Quit", fg = "red", command = frame.quit)
        self.btnQuit.pack(side=LEFT)

        self.btnHello = Button (
            frame, text = "Hello, world!", command = self.say_hello)
        self.btnHello.pack(side=RIGHT)
        
    def say_hello(self):
        print("Hello, world!")

root = Tk()
app = App(root)
root.mainloop()
#root.destroy()