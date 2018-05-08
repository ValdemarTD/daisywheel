#!/usr/bin/env python

from inputs import get_gamepad
import numpy as np
import pyautogui as pg
from time import sleep

pg.PAUSE = .01

class MouseSim:
    def __init__(self):
        self.events = get_gamepad()
#Ignores the ping every action sends
        self.ignore = 'SYN_REPORT'
#Defines button names
        self.var1name = "ABS_HAT0X"
        self.b1 = "BTN_NORTH"
        self.b2 = "BTN_WEST"
        self.b3 = "BTN_EAST"
#Defines other unchanging variables
        self.maxclickmode = 3
#Sets up changing variables with initial values
        self.clickmode = 0
        self.vert = False
        self.pos = pg.position()
        self.screensize = pg.size()
        self.mousespeed = 120
        self.mouseX = self.pos[0]
        self.mouseY = self.pos[1]
        self.mousebutton = 'left'
        self.movementactive = False
        self.direction = 0
    def exitmousemode(self):
        print("Normally this would exit mousemode, but for now, have some filler text!")
        exit()
#    def mover(self):
#        print("GO!")
#        print(self.events)
#        if self.vert == True:
#            pg.moveTo(self.mouseX, self.mouseY + self.direction*self.mousespeed/30)
#        elif self.vert == False:
#            pg.moveTo(self.mouseX + self.direction*self.mousespeed/30, self.mouseY)
#        sleep(.1)

    def mouse(self):
        while True:
            self.events = get_gamepad()
            self.pos = pg.position()
            self.mouseX = self.pos[0]
            self.mouseY = self.pos[1]
            for event in self.events:
#                print(self.events)
#                print(event.code)
#                print(event.state)
                if event.code == self.b3 and event.state == 1:
                    self.clickmode = self.clickmode + 1
                    print("Current button:"),
                    if self.clickmode > self.maxclickmode:
                        self.clickmode = 0
                        self.mousebutton = 'left'
                        print(self.mousebutton)
                    elif self.clickmode == 1:
                        self.mousebutton = 'middle'
                        print(self.mousebutton)
                    elif self.clickmode == 2:
                        self.mousebutton = 'right'
                        print(self.mousebutton)
                    elif self.clickmode == 3:
                        self.mousebutton = 'exit mousemode'
                        print(self.mousebutton)
                elif event.code == self.b2 and event.state == 1:
                    self.vert = not self.vert
                    if self.vert == True:
                        print('Mousemode: Vertical')
                    elif self.vert == False:
                        print('Mousemode: Horizontal')
                elif event.code == self.b1 and self.clickmode != 3:
                    if event.state == 1:
                        pg.mouseDown(x = self.mouseX, y = self.mouseY, button = self.mousebutton)
                    elif event.state == 0:
                        pg.mouseUp(x = self.mouseX, y = self.mouseY, button = self.mousebutton)
                elif event.code == self.b1 and self.clickmode == 3:
                    MouseSim.exitmousemode(self)
                elif event.code == self.var1name:
                    self.movementactive = True
                    self.direction = event.state
                    print(self.direction)
                    if event.state == 0:
                        self.movementactive = False
                    while self.movementactive == True:
                        self.pos = pg.position()
                        self.mouseX = self.pos[0]
                        self.mouseY = self.pos[1]
                        self.events = get_gamepad()
                        for event in self.events:
                            if event.code == self.var1name and event.state == 0:
                                self.movementactive = False
                            else:
                                pass
                        if self.vert == True:
                            pg.moveTo(self.mouseX, self.mouseY + self.direction*self.mousespeed/30)
                        elif self.vert == False:
                            pg.moveTo(self.mouseX + self.direction*self.mousespeed/30, self.mouseY)
                sleep(.01)

#                elif event.code == self.var1name:
#                    self.pos = pg.position()
#                    self.mouseX = self.pos[0]
#                    self.mouseY = self.pos[1]
#                    print(event.state)
#                    self.movementactive = True
#                    while self.movementactive == True:
#                        print(self.movementactive)
#                        self.pos = pg.position()
#                        self.mouseX = self.pos[0]
#                        self.mouseY = self.pos[1]
#                        for event in self.events:
#                            if event.code != self.ignore:
#                                print(event.code)
#                                print(event.state)
#                            elif event.code != self.var1name and event.code != self.ignore:
#                                break
#                            if event.code == self.var1name:
#                                self.direction = event.state
#                            elif event.code == self.var1name and abs(event.state) != 1:
#                                self.movementactive = False
#                                print('Movement ended')
#                        if self.vert == True:
#                            pg.moveTo(self.mouseX, self.mouseY + self.direction*self.mousespeed/30)
#                        elif self.vert == False:
#                            pg.moveTo(self.mouseX + self.direction*self.mousespeed/30, self.mouseY)
#                        self.events = get_gamepad()

if __name__ == '__main__':
    mousesim = MouseSim()
    mousesim.mouse()
