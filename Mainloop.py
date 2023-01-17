from GUI import GUI
from Duck import Duck

class Mainloop():
    def __init__(self, tickspeed=500):
        self.gui = GUI()
        self.duck = Duck([self.gui.height, self.gui.width])
        self.tickspeed = tickspeed

        self.duckControl()

        self.startGame()

    def duckControl(self):
        if self.duck.decideToMove():
            x,y = self.duck.getPos()
            self.gui.moveDuck(x,y)
        else:
            x,y = self.duck.getPos()
            self.gui.drawIdleDuck(x,y)

        self.gui.root.after(self.tickspeed, self.duckControl)

    def startGame(self):
        self.gui.root.mainloop()