#!/usr/bin/env python

import pyautogui as pg
import numpy as np
from inputs import get_gamepad
import threading

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

    def cycler(self):
        #Prints the first character "block" and spacing lines.
        print(self.layout[self.var1])
        print("------------------------")
        print("------------------------")
        #Main loop
        while True:
            #Checks for updates
            self.events = get_gamepad()
            #Processes updates
            for event in self.events:
                #Increments var1 by 1 or -1 if appropriate
                if(event.code == self.var1name) and (-1 < self.var1 + event.state < self.var1max+1):
                    self.var1 = self.var1 + event.state
                    #Shows new character "block" if appropriate. If var1 has been changed, it will also unlock var2
                    if(event.state != 0):
                        self.var2lock == False
                        print(self.layout[self.var1])
                        print("------------------------")
                        print("------------------------")
                #Checks if one of the buttons has been pressed
                elif(event.code == self.b1 or event.code == self.b2 or event.code == self.b3):
                    #Checks if var2 has already been entered
                    if(self.var2lock == False):
                        #Set var2 to corresponding button value. Locks var2. Prints specified character "line" and spacers.
                        if(event.code == self.b1 and event.state == 1):
                            self.var2 = 0
                            self.var2lock = True
                            print(self.layout[self.var1,self.var2])
                            print("------------------------")
                            print("------------------------")
                        elif(event.code == self.b2 and event.state == 1):
                            self.var2 = 1
                            self.var2lock = True
                            print(self.layout[self.var1,self.var2])
                            print("------------------------")
                            print("------------------------")
                        elif(event.code == self.b3 and event.state == 1):
                            self.var2 = 2
                            self.var2lock = True
                            print(self.layout[self.var1,self.var2])
                            print("------------------------")
                            print("------------------------")
                    #Checks if var2 has been locked
                    elif(self.var2lock == True):
                        #Set var3 to corresponding button value. Prints selection and spacers. Presses specified button. Prints current character "block" and spacers,
                        #and unlocks var2
                        #Essentially prints and then goes back to the beginning.
                        if(event.code == self.b1 and event.state == 1):
                            self.var3 = 0
                            print(self.layout[self.var1,self.var2,self.var3])
                            pg.press([self.layout[self.var1,self.var2,self.var3]])
                            print("------------------------")
                            print("------------------------")
                            print(self.layout[self.var1])
                            print("------------------------")
                            print("------------------------")
                            self.var2lock = False
                        elif(event.code == self.b2 and event.state == 1):
                            self.var3 = 1
                            print(self.layout[self.var1,self.var2,self.var3])
                            pg.press([self.layout[self.var1,self.var2,self.var3]])
                            print("------------------------")
                            print("------------------------")
                            print(self.layout[self.var1])
                            print("------------------------")
                            print("------------------------")
                            self.var2lock = False
                        elif(event.code == self.b3 and event.state == 1):
                            self.var3 = 2
                            print(self.layout[self.var1,self.var2,self.var3])
                            pg.press([self.layout[self.var1,self.var2,self.var3]])
                            print("------------------------")
                            print("------------------------")
                            print(self.layout[self.var1])
                            print("------------------------")
                            print("------------------------")
                            self.var2lock = False


#Runs.
if __name__ == '__main__':
    keysim = Keysim()
    keysim.cycler()
