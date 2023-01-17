import tkinter as tk
from tkinter import *
import random

class Duck():
    def __init__(self, bounds, x=250, y=250):
        self.xBound = bounds[0]
        self.yBound = bounds[1]
        self.x = x
        self.y = y
        self.emotionalState = 0

        self.phrases = ["Hello", "I am duck", "Quack"]
        # self.quack()

    def getPos(self):
        return self.x, self.y
    
    def decideToMove(self):
        decision = random.randint(0, 100)
        if (decision > 95):
            self.x = random.randint(10, self.xBound - 10)
            self.y = random.randint(310, self.yBound - 10)
            return True
        else:
            return False
