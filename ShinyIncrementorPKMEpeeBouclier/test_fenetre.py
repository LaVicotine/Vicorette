# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 01:04:56 2019

@author: vicot
"""

from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Shiny incrementator")

def launch():
    print("Coucou")

def exit1():
    exit()
    
label1=Label(window,text="Shiny incrementator 1.0",relief="solid",width=20,font=("arial",19,"bold"))
label1.place(x=90, y=53)

b1=Button(window,text="Start",width=12,bg="brown",fg="white",command=launch)
b1.place(x=150,y=380)

b2=Button(window,text="Exit", width=15,bg="brown",fg="white",command=exit1)
b2.place(x=280,y=380)