import tkinter as tk
from tkinter import filedialog
#this file contains various user interfacing methods used throughout the program.

#initialize tk windows (gets rid of blank box)
def init():
    tk.Tk().withdraw()
#show popup message to user with message msg
def popupmsg(msg):
    tk.messagebox.showinfo("BeatmapSharing",msg)

#prompt to select directory in filesystem
def getdirectory():
    return filedialog.askdirectory()

#prompt to select file in filesystem
def getfilename():
    return filedialog.askopenfilename()