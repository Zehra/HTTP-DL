"""
Simple tool to download a file via HTTP.
Very basic, can be used as template/boilerplate code.

License: CC0-1.0
"""

import requests
import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk

Title="Zehra's HTTP Downloader"

httpdl = tk.Tk()
httpdl.title(Title)
httpdl.geometry("292x173")
httpdl.configure(bg="black")

wincanvas = Canvas(httpdl,width=268, height=44,
highlightthickness=0, bg='light blue')
wincanvas.place(x = 12,y = 12)
# Good canvas example.

dlLink = StringVar()

txtLink = Entry(httpdl, bg='black', foreground='white', textvariable=dlLink) #, font=("Arial Black", 20))
txtLink.place(x=18, y=32, width=256, height=20)



def Download(dlurl : str):
    # Somewhat good examples of splitting strings, slicing them and more.
    try:
        dlurllen = len(dlurl)
        if dlurllen > 7: # 7 == http://
            dcmpvar = dlurl[7:dlurllen]
            dprcmpvar = dlurl[:7]
            # Useful examples of string slicing.
            #print(dcmpvar)
            #print(dprcmpvar)
            plwcmp = dprcmpvar.lower()
            if plwcmp == "http://":
                items = dlurl.split('/')
                itemcount = len(items)
                f1 = items[(itemcount-1)]
                #print(f1)
                f1len = len(f1)
                #print(f1len)
                if f1len >= 0:
                    filename = f1
                    #print(filename)
                else:
                    filename = "recent"
                try:
                    filemake = open(filename, "w")
                    #print(filemake)
                except:
                    print("Error on attempting to create file.")
                
                headers = {'user-agent': 'HTTP-DL: v0.0.1 Prototype'}
                req = requests.get(dlurl, headers=headers, allow_redirects=False, timeout=5.00)
                if req.status_code == requests.codes.ok:
                    filemake.writelines(req.text)
                    filemake.close()
                else:
                    print("Download attempt was not successful.")
                    filemake.close()
            else:
                print("Only HTTP requests supported.")    
                             
    except:
        print("Error on URL value")



def cmdDL_click():
    global dlLink
    download(dlLink)

def cmdClipDL_click():
    global dlLink
    dlLink = httpdl.clipboard_get()
    txtLink.delete(0,END)
    txtLink.insert(0,dlLink)
    #^ Good example of modifying text in an Entry widget.
    #print(dlLink)
    Download(dlLink)


dFrom = Label(httpdl, text="Download from", bg='light blue', foreground='black')#, font=("Arial Black", 10))
dFrom.place(x=24, y=12, width=100, height=20)
#^ Useful example of a custom label and modded size, plus commented font/size option.
cmdcmdDL = Button(httpdl, text="Download entered link", bg='light blue', command=cmdDL_click)
cmdcmdDL.place(x=12, y=72, height=23, width=268)
# Useful examples of a button.
cmdClipDL = Button(httpdl, text="Download the link on clipboard", bg='light blue', command=cmdClipDL_click)
cmdClipDL.place(x=12, y=101, height=59, width=268)
# Useful example of clipboard being used.


httpdl.mainloop()

# TODO: 
# Add download progress indication with a text widget or similar.
# Cleanup code.
# Also make it more work-able.

