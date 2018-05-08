#!/usr/bin/env python

import pyautogui as pg
import numpy as np
from inputs import get_gamepad
import threading
from time import sleep

#Defines global characters for layouts. Makes changing layouts faster
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
        #Checks for gamepad events
        self.events = 'null'
        #Defines the keyboard layout where any character is located at self.layout[var1,var2,var3].
        self.layout = np.array([[[a,b,c],[d,e,f],[g,h,i]],
                                [[j,k,l],[m,n,o],[p,q,r]],
                                [[s,t,u],[v,w,x],[y,z,0]],
                                [[1,2,3],[4,5,6],[7,8,9]],
                                [['space',".","."],['enter',"!",'""'],["''","?",'backspace']],
                                [['left', 'down', 'delete'],['tab','up','esc'],['/','~','right']]])
        #Sets the maximum value for var1. Allows easy expansion of layout.
        self.var1max = 4
        #Sets initial values for var1, var2, and var3
        self.var1 = 0
        self.var2 = 0
        self.var3 = 0
        #Assigns the event codes from get_gamepad() to specific variables for easier controller layout changes.
        self.var1name = "ABS_HAT0X"
        self.b1 = "BTN_NORTH"
        self.b2 = "BTN_WEST"
        self.b3 = "BTN_EAST"
        #Tells whether or not var2 has been entered. Set to false at the beginning.
        self.var2lock = False
        self.delay = 1
        self.direction = 0
    def cycler(self):
        while True:
            self.var1 = self.var1 + self.direction
            sleep(self.delay)
    def watcher(self):
        self.events = get_gamepad()
        for event in self.events:
            if (event.code == self.var1name):
                self.direction = event.state
                if
