'''
Created on Nov 1, 2014

@author: chris
'''

from Tkinter import *

def printHello(thisWidget):
    print "Hello"
    
#create the Window
root = Tk()

#modify root Window
root.title("Simple GUI")
root.geometry("200x250")

app = Frame(root)
app.grid()
label = Label(app, text = "This is a label!")
label.bind('<Button-1>', printHello)
label.grid()

button = Button(app, text = "This is a button!")
button.grid()

button2 = Button(app)
button2.grid()
button2.configure(text="I am button 2")

button3 = Button(app)
button3.grid()
button3["text"] = "Button 3"
#kick off the event loop
root.mainloop()