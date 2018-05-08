#!/usr/bin/env python

import pyautogui as pg
import numpy as np
import time
from inputs import get_gamepad


a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'
h = 'h'
i = 'i'
j = 'j'
k = 'k'
l = 'l'
m = 'm'
n = 'n'
o = 'o'
p = 'p'
q = 'q'
r = 'r'
s = 's'
t = 't'
u = 'u'
v = 'v'
w = 'w'
x = 'x'
y = 'y'
z = 'z'


class Keysim:
    def __init__(self):
        self.tolerance = 9000
        self.can_output = False
        self.var1 = 0
        self.var2 = 0
        self.xval = 0
        self.yval = 0
        self.events = get_gamepad()
        self.dvorak = np.array([[a,o,e,u,i],
                               [d,h,t,n,s],
                               [p,y,f,g,c],
                               [r,l,q,j,k],
                               [x,b,m,w,v],
                               [z,1,2,3,4],
                               [5,6,7,8,9],
                               [0,'.',',','/',"'"]], dtype = str)
        self.qwerty = np.array([[q,w,e,r,t],
                               [y,u,i,o,p],
                               [a,s,d,f,g],
                               [h,j,k,l,z],
                               [x,c,v,b,n],
                               [m,1,2,3,4],
                               [5,6,7,8,9],
                               [0,'.',',','/',"'"]], dtype = str)
        self.alpha =  np.array([[a,b,c,d,e],
                               [f,g,h,i,j],
                               [k,l,m,n,o],
                               [p,q,r,s,t],
                               [u,v,w,x,y],
                               [z,1,2,3,4],
                               [5,6,7,8,9],
                               [0,'.',',','/',"'"]], dtype = str)
        self.input_type = self.dvorak
        self.selection = 'alpha'
        self.mouse = False
        self.mouseSpeed = 150
    def mousecode(self):
        #Placeholder
        print("This is placeholder code, and is next on the todo list.")
    def input_select(self):
        self.selection = input('Which layout would you like? (please type dvorak, qwerty, or abcde)')
        if(self.selection == 'dvorak'):
            self.input_type = self.dvorak
        elif(self.selection == 'qwerty'):
            self.input_type = self.qwerty
        elif(self.input_type == 'abcde'):
            self.input_type = self.alpha
    def test(self):
        self.events = get_gamepad()
#        var1 = input('What is the first value? (0-7)')
#        var2 = input('What is the second value? (0-4)')
#        print(self.dvorak[self.var1,self.var2])
#        print(self.qwerty[var1,var2])
#        print(self.alpha[var1,var2])
        for event in self.events:
            if(event.code == 'BTN_START'):
                self.mouse = not self.mouse
            if(self.mouse == True):
                KeySim.mousecode()
            elif(self.mouse == False):
                if(event.code == 'ABS_Z' and event.state > 20):
                    pg.keyDown('shift')
                elif(event.code == 'ABS_Z' and event.state < 20):
                    pg.keyUp('shift')
                if(event.code == 'ABS_Y'):
                    self.yval = event.state
                elif(event.code == 'ABS_X'):
                    self.xval = event.state
                if(self.yval < -self.tolerance) and (abs(self.xval) < self.tolerance):
                    self.var1 = 0
                    self.can_output = True
                elif(self.yval < -self.tolerance) and (self.xval > self.tolerance):
                    self.var1 = 1
                    self.can_output = True
                elif(self.yval < -self.tolerance) and (self.xval < -self.tolerance):
                    self.var1 = 2
                    self.can_output = True
                elif(abs(self.yval < self.tolerance)) and (self.xval < -self.tolerance):
                    self.var1 = 3
                    self.can_output = True
                elif(abs(self.yval < self.tolerance)) and (self.xval > self.tolerance):
                    self.var1 = 4
                    self.can_output = True
                elif(self.yval > self.tolerance) and (self.xval < -self.tolerance):
                    self.var1 = 5
                    self.can_output = True
                elif(self.yval > self.tolerance) and (self.xval > self.tolerance):
                    self.var1 = 6
                    self.can_output = True
                elif(self.yval > self.tolerance) and (abs(self.xval) < self.tolerance):
                    self.var1 = 7
                    self.can_output = True
                else:
                    self.can_output = False
                if(event.code == 'BTN_WEST') and (event.state == 1):
                    self.var2 = 0
                    pg.press(self.input_type[self.var1,self.var2])
                elif(event.code == 'BTN_EAST') and (event.state == 1):
                    self.var2 = 1
                    pg.press(self.input_type[self.var1,self.var2])
                elif(event.code == 'BTN_SOUTH') and (event.state == 1):
                    self.var2 = 2
                    pg.press(self.input_type[self.var1,self.var2])
                elif(event.code == 'BTN_NORTH') and (event.state == 1):
                    self.var2 = 3
                    pg.press(self.input_type[self.var1,self.var2])
                elif(event.code == 'BTN_TR') and (event.state == 1):
                    self.var2 = 4
                    pg.press(self.input_type[self.var1,self.var2])
#            print(event.ev_type, event.code, event.state)


if __name__ == '__main__':
    keysim = Keysim()
#    keysim.input_select()
while True:
    keysim.test()
