# for python 2
import hashlib
import ttk
from Tkinter import *
# for python 3
"""
import hashlib
from tkinter import ttk
from tkinter import *
"""

tk = Tk()
input_ = StringVar()

def callback():
    result = input_.get()
    sha = hashlib.sha256(result.encode())
    out = sha.hexdigest()
    if len(result) == 0:
        IN_la = Label(tk, text = "Input Plan Text again")
        IN_la.pack()
    else:
        OUT_lb = Label(tk, text = out)
        OUT_lb.pack()
        
tk.title("SHA 256 CONVERTER ")
tk.geometry('500x600')
IN_lb = Label(tk, text = "Input Plan Text")
IN_lb.pack()
textbox = ttk.Entry(tk, width=30, textvariable=input_)
textbox.pack()
button = Button(tk, text = "Translate", command = callback)
button.pack()

tk.mainloop()
