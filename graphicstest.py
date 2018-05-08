#!/usr/bin/env python

import pygame
import numpy as np

pygame.init()

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

fillertext = np.array([[[a,b,c],[d,e,f],[g,h,i]],
                        [[j,k,l],[m,n,o],[p,q,r]],
                        [[s,t,u],[v,w,x],[y,z,0]],
                        [[1,2,3],[4,5,6],[7,8,9]],
                        [['space',".","."],['enter',"!",'""'],["''","?",'backspace']]])

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

size = (800, 600)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)



font = pygame.font.SysFont('Calibri', 50, True, False)

text = font.render("".join(map(str, fillertext)), True, BLACK)

screen.blit(font.render("test", True, WHITE), [250,250])
pygame.display.flip()

while True:


    pygame.display.flip()
