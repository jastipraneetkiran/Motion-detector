import sys
import sys
import os
import Tkinter
import tkMessageBox
top=Tkinter.Tk()

def helloCallBack():
    os.system('python3 mainplot.py')

B=Tkinter.Button(top,text="start",command= helloCallBack)
B.pack()
top.mainloop()

