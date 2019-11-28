# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 01:45:11 2019
Finished on Thu Nov 28 00:29:49 2019

@author: vicot
"""

import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import pytesseract

#Ask which pokemon your hunting
pkmn_name = input('Enter your input:')

#Get current incrementation number
f= open("number.txt","r")
inc= int(f.read())
f.close()

bool = 1

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)

chrome = [(hwnd, title) for hwnd, title in winlist if 'projecteur' in title.lower()]
chrome = chrome[0] 
hwnd = chrome[0]

left, top, right, bot = win32gui.GetWindowRect(hwnd)
w = right - left
h = bot - top

while True:
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    
    saveDC.SelectObject(saveBitMap)
    
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    w, h = img.size
    
    #Ligne a changé s'il faut mieux capturer le nom
    img = img.crop((0.79*w, 0.07*h, w-w*0.12, h-(0.9*h)))
    
    #Décommenter la ligne en dessous pour voir l'image coupée
    #img.show()
    
    pytesseract.pytesseract.tesseract_cmd = 'tesseract.exe'
    output = pytesseract.image_to_string(img.convert("RGB"), lang='eng')
    if pkmn_name in output and bool:
        inc=inc+1
        bool=0
        print(inc)
        f= open("number.txt","w")
        f.write(str(inc))
        f.close()
    elif pkmn_name in output:
        bool=0
    else:
        bool=1 
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
        
