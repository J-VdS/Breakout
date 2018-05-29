from tkinter import *

class paddle(object):
    def __init__(self, canvas, width=100, color='#0000ff'):
        self.canvas = canvas
        self.width = self.canvas.winfo_width()

        x = int(self.width/2 - width/2)
        y = self.canvas.winfo_height() - 50
        

        
        self.id = self.canvas.create_rectangle(x, y, x+width, y+10, fill=color)
        self.vx = 0
        self.canvas.bind_all('<KeyPress - Left>', self.left)
        self.canvas.bind_all('<KeyPress - Right>', self.right)

    def left(self, evt):
        self.vx = -4
        

    def right(self, evt):
        self.vx = 4
        

    def move(self):
        co = self.canvas.coords(self.id)
        self.vx = self.vx*(0 < co[0] + self.vx)* (co[2] + self.vx < self.width)
        self.canvas.move(self.id, self.vx, 0)
        
        
    def getcoords(self):
        return self.canvas.coords(self.id)
