from tkinter import *
import tkinter as tk
from Canvas import Canvas
from Duck import Duck

class GUI(Canvas):
    def __init__(self, width=500, height=500):
        # initialize the information for the root frame
        self.root = Tk()
        self.root.geometry("%dx%d+0+0" % (width, height))
        self.root.title("Duck Garden Pre-Alpha")
        self.root.resizable(0,0)
        self.height = height
        self.width = width
        Canvas.__init__(self, self.root, self.width, self.height)
    