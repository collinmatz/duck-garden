# class for the screen the player sees
from tkinter import *
import tkinter as tk
import time
from random import random

class Canvas():
    def __init__(self, root, width, height):
        self.canvas = tk.Canvas(root, width=width, height=height, bg=self.getBGFromTime(), highlightthickness=0)
        self.canvas.pack()
        self.canvasHeight = height
        self.canvasWidth = width
        self.bg = self.getBGFromTime()
        self.grassColor = self.getGrassColorFromTime()
        self.duckFacing = "R"

        # draw main game elements
        self.drawGrass()
        self.drawSun()

        # create duck
        self.duckFrame = PhotoImage(file="assets/duck-frames/duck0.png")
        self.duck = self.canvas.create_image(250, 250, image=self.duckFrame, tags="duck")

    # generate the color for the sky based on local device time
    def getBGFromTime(self):
        # sky color at day: (40, 180, 250)
        rgb = [40, 180, 250]
        hour = time.localtime().tm_hour
        # rgb[1] -= hour * 3
        # rgb[2] -= hour * 3
        return("#%02x%02x%02x" % tuple(rgb)) # convert to hex

    def getGrassColorFromTime(self):
        rgb = [63, 155, 11]
        hour = time.localtime().tm_hour
        return("#%02x%02x%02x" % tuple(rgb)) # convert to hex

    def drawGrass(self):
        surfacePointsList = [self.canvasWidth, self.canvasHeight, 0, self.canvasHeight, 0, self.canvasHeight-350, self.canvasWidth, self.canvasHeight-350]
        self.canvas.create_polygon(surfacePointsList, fill=self.grassColor)
        for i in range(100):
            x = (random() * self.width)
            y = (500 - random() * 345)
            self.canvas.create_oval(x-1, y-1, x+1, y+1, fill="#00800d", outline="")
    
    def drawSun(self):
        surfacePointsList = [10, 0, 60, 0, 60, 50, 10, 50]
        self.canvas.create_polygon(surfacePointsList, fill="yellow")

    def drawIdleDuck(self, duckx, ducky, state=0):
        if (self.duckFacing == "L"):
            if (state == 0):
                self.duckFrame = PhotoImage(file="assets/duck-frames/duck0.png")
                self.canvas.itemconfig(self.duck, image=self.duckFrame)
                self.canvas.after(250, lambda: self.drawIdleDuck(duckx, ducky, 1))
            else:
                self.duckFrame = PhotoImage(file="assets/duck-frames/duck1.png")
                self.canvas.itemconfig(self.duck, image=self.duckFrame)
        else:
            if (state == 0):
                self.duckFrame = PhotoImage(file="assets/duck-frames/duckFlip0.png")
                self.canvas.itemconfig(self.duck, image=self.duckFrame)
                self.canvas.after(250, lambda: self.drawIdleDuck(duckx, ducky, 1))
            else:
                self.duckFrame = PhotoImage(file="assets/duck-frames/duckFlip1.png")
                self.canvas.itemconfig(self.duck, image=self.duckFrame)

    def moveDuck(self, duckx, ducky, state=0):
        currentCoords = self.canvas.coords(self.duck)
        xDist = currentCoords[0] - duckx
        yDist = currentCoords[1] - ducky
        nextx = 0
        nexty = 0

        if (xDist != 0 or yDist != 0):
            if (xDist < 0):
                nextx = currentCoords[0] + 1
                self.duckFacing = "R"
            elif (xDist > 0):
                nextx = currentCoords[0] - 1
                self.duckFacing = "L"
            if (yDist < 0):
                nexty = currentCoords[1] + 1
            elif (yDist > 0):
                nexty = currentCoords[1] - 1

        if (self.duckFacing == "L"):
            if (state == 0):
                self.duckFrame = PhotoImage(file="assets/duck-frames/duckWalk0.png")
                self.canvas.itemconfig(self.duck, image=self.duckFrame)
                self.canvas.after(250, lambda: self.moveDuck(duckx, ducky, 1))

            else:
                self.duckFrame = PhotoImage(file="assets/duck-frames/duckWalk1.png")
                self.canvas.itemconfig(self.duck, image=self.duckFrame)
        else:
            if (state == 0):
                self.duckFrame = PhotoImage(file="assets/duck-frames/duckWalkFlip0.png")
                self.canvas.itemconfig(self.duck, image=self.duckFrame)
                self.canvas.after(250, lambda: self.moveDuck(duckx, ducky, 1))

            else:
                self.duckFrame = PhotoImage(file="assets/duck-frames/duckWalkFlip1.png")
                self.canvas.itemconfig(self.duck, image=self.duckFrame)


        self.canvas.coords(self.duck, nextx, nexty)

