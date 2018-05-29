from tkinter import *
import random

class ball(object):
    def __init__(self, canvas, paddle, veld):
       
        self.canvas = canvas
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.paddle = paddle

        self.r = 5 #straal
        self.vx = random.choice([-2, -1, 1, 2]) #random.choice([-3, -2, -1, 1, 2, 3])
        self.vy = -3
        self.maxvx = 5
        self.maxvx_id = self.canvas.create_text(2, self.height-2, anchor=SW, \
                                text='{a}'.format(a=self.vx))

        #self.id = canvas.create_oval(self.width/2-5, 0, self.width/2+5, 10, fill='#abab00')
        
        
        self.id = self.canvas.create_oval(int(self.width/2 - self.r),\
                  self.height -50-2*self.r, int(self.width/2+self.r), \
                  self.height-50, fill='#abab00')

        self.veld = veld
        self.blokken = veld.get_blokken()            

        
    def move(self):
        co = self.canvas.coords(self.id)

        self.hitblok(co)
        
        if 0 >= co[0] or co[2] > self.width:
            self.vx *= -1
        if 0 >= co[1] :
            self.vy *= -1
        elif self.hitpaddle(co):
            self.vy *= -1
            self.vx += - 1*(self.paddle.vx < 0)*(abs(self.vx - 1) < self.maxvx)\
                       + 1*(self.paddle.vx > 0)*(self.vx + 1 <self.maxvx)
        self.canvas.itemconfig(self.maxvx_id, text='{a}'.format(a=self.vx))
        '''        
        self.vx = self.vx - 2*self.vx *(co[0]+self.vx <= 0) \
                  - 2*self.vx *(co[2]+self.vx >= self.width)
        self.vy = self.vy - 2*self.vy * (co[1] + self.vy < 0)
        '''
        
        if co[3] > self.height:
            #game over implementatie ontbreekt hier nog
            self.vy *= -1
        
        self.canvas.move(self.id, self.vx, self.vy)

    def hitpaddle(self, co_bal):
        co_pad = self.paddle.getcoords()
        if self.vy < 0:
            return False        
        elif co_pad[1] <= co_bal[3] <= co_pad[3]:
            if co_pad[0] <= co_bal[0]+self.r <= co_pad[2]:
                return True
        return False

    def hitblok(self, co_bal):
        
        for i in self.blokken.keys():
            if i[0] <= co_bal[1] <= i[1] or i[0] <= co_bal[3] <= i[1]: 
                for blok in self.blokken[i]:
                    co_blok = blok.get_coords()
                    if co_blok[0] <= co_bal[0] and co_bal[2] <= co_blok[2]:
                        self.vy *= -1
                        
                        blok.verdwijn()
                        self.blokken[i].remove(blok)

                        if len(self.blokken[i]) == 0:
                            del self.blokken[i]

                        return
                    elif co_blok[0] <= co_bal[0] <= co_blok[2] and self.vx < 0:
                        self.vx *= -1
                        blok.verdwijn()
                        self.blokken[i].remove(blok)

                        if len(self.blokken[i]) == 0:
                            del self.blokken[i]
                            
                        
                        return
                    elif co_blok[0] <= co_bal[2] <= co_blok[2] and self.vx > 0:
                        self.vx *= -1
                        blok.verdwijn()
                        self.blokken[i].remove(blok)

                        if len(self.blokken[i]) == 0:
                            del self.blokken[i]
                            
                        
                        return

        if len(self.blokken.keys()) == 0:
                self.restart()

    def restart(self):
        self.veld.makeveld()
        self.blokken = self.veld.get_blokken()
        co = self.canvas.coords(self.id)
        self.canvas.move(self.id, self.width/2 - self.r - co[0], \
                         self.height -50-2*self.r - co[1])
        self.vy = -1 * abs(self.vy)

        #co_pad = 
        
    
