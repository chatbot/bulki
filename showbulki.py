#!/usr/bin/python
import pygame, os, time, random, sys
from pygame.locals import *
from numpy import *
from ctypes import *
from math import *


screen = None
data = None
w = None
h = None
s = None
oldpos = -1
pos = 0
posdiff = 1
maxpos = 0
header_size = 8
image_size = 0
f = None
font = None

def start():
    global data, screen, w, h, s, image_size, f, font, maxpos


    filename = sys.argv[1]
    f = open(filename)
    dim = frombuffer(f.read(8),int,2)
    w = dim[0]; h = dim[1]
    print 'dimensions: %i, %i' % (w,h)
    image_size = w*h*3

    pygame.init()
    window = pygame.display.set_mode((w,h),RESIZABLE)
    pygame.display.set_caption("showbulki")
    screen = pygame.display.get_surface()

    maxpos = os.path.getsize(filename)/image_size-1

    font = pygame.font.Font(None,36)

def input(events):
    global pos,maxpos,posdiff
    for event in events:
        if event.type == VIDEORESIZE:
            pygame.display.set_mode(event.size, RESIZABLE)
            #print event
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit(0)
            elif event.key == K_PAGEDOWN:
                pos -= 50
            elif event.key == K_PAGEUP:
                pos += 50
            elif event.key == K_RIGHTBRACKET:
                posdiff += 1
            elif event.key == K_LEFTBRACKET:
                posdiff -= 1
                if posdiff < 1:
                    posdiff = 1

    keystate = pygame.key.get_pressed()
    if keystate[K_LEFT]:
        pos-=posdiff
    elif keystate[K_RIGHT]:
        pos+=posdiff


def draw():
    global screen,w,h,data,s, f, pos, oldpos, maxpos
    if pos < 0:
        pos = 0
    elif pos > maxpos:
        pos = maxpos

    if oldpos != pos:
        oldpos = pos
    else:
        return



    imgsize = w*h*3
    f.seek(header_size + image_size*pos)
    s = f.read(image_size)
    surf = pygame.image.frombuffer(s,(w,h),'RGB')
    rect = (0,0,w,h)
    screen.blit(surf,rect)


    label = font.render(str(pos), 1, (0, 0, 255))
    labrect  = (0,0,label.get_width(),label.get_height())
    screen.blit(label,labrect)
    pygame.display.flip()




start()
while True:
    input(pygame.event.get())
    draw()
    time.sleep(0.03)


    
