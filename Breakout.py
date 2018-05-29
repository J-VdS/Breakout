from tkinter import *
import time,random

#andere files
from ball import ball
from paddle import paddle



class blok(object):
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.co = (x1, y1, x2, y2)
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def verdwijn(self):
        self.canvas.delete(self.id)

    def get_coords(self):
        return self.co

class veld(object):
    def __init__(self, canvas, rows=5, columns=10):
        self.canvas = canvas
        self.window = (self.canvas.winfo_width(), self.canvas.winfo_height())
        self.width = (self.window[0] - 2) / columns
        self.height = 20
        self.rows = rows
        self.columns = columns
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue']


        self.makeveld()

        
    def makeveld(self):
        self.bveld = {}
        for rij in range(self.rows):
            y = 20+rij*self.height
            l = []
            color = self.colors[rij % len(self.colors)]
            for kolom in range(self.columns):
                l.append(blok(self.canvas, 1+kolom*self.width, y,  1+(kolom+1)*self.width, \
                              y+self.height, color))
            self.bveld[(y, y+self.height)] = l
            del l
        #print(self.veld)
        #print(self.bveld.keys())
        
    def get_blokken(self):
        return self.bveld
    



tk = Tk()
tk.resizable(0,0)
tk.wm_attributes('-topmost', 1)
tk.title('Atari breakout')
canvas = Canvas(tk, width=500, height=350, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
p = paddle(canvas)
v = veld(canvas)
b = ball(canvas, p, v)



alive = True
def end(evt):
    global alive
    alive = False
canvas.bind_all('<space>', end)


while alive:
    p.move()
    b.move()
    tk.update()
    tk.update_idletasks()
    time.sleep(0.015)

time.sleep(1)
canvas.delete('all')
tk.destroy()
    
