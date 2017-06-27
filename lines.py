import pygame
from math import sin, cos
import sys

pygame.init()

clock = pygame.time.Clock()

displaywidth = 640
displayheight = 480

display = pygame.display.set_mode((displaywidth, displayheight))

'''colourz'''
black = (0 ,0 ,0)
white = (255, 255, 255)
red = (255, 0, 100)
green = (0, 255, 150)
blue = (0, 150, 255)

'''environment box attributez'''
vx1, vy1, vx2, vy2 = 50, 80, 150, 80

b1x, b1y, b1w, b1h = 0, 0, 200, 200
b2x, b2y, b2w, b2h = 220, 0, 200, 200
b3x, b3y, b3w, b3h = 440, 0, 200, 200
boundarythickness = 3

'''player attributez'''
heading = 0.0
pspeed = 2
px, py = 100, 100

#########################
'''GAME LOOP N SHIT'''
#########################

while True:
    display.fill(black)

    '''ABSOLUTE MAP'''
    '''player's centre location dot'''
    pygame.draw.rect(display, red, (px -1, py-1, 3, 3), 0)

    '''line coming out of the player, showing playa heading'''
    pygame.draw.line(display, blue, (px,py), (cos(heading)*10 + px, sin(heading)*10 + py), 1)

    '''this is a line'''
    pygame.draw.line(display, red, (vx1, vy1), (vx2, vy2), 2)

    '''draw window enclosing box'''
    pygame.draw.rect(display, green, (b1x,b1y,b1w,b1h), boundarythickness)



    '''RELATIVE MAP'''
    '''transform vertecies relative to the player'''
    tx1 = vx1 - px
    ty1 = vy1 - py
    tx2 = vx2 - px
    ty2 = vy2 - py

    '''rotate them around the playaz' view'''
    tz1 = tx1 * cos(heading) + ty1 * sin(heading)
    tz2 = tx2 * cos(heading) + ty2 * sin(heading)
    tx1 = tx1 * sin(heading) - ty1 * cos(heading)
    tx2 = tx2 * sin(heading) - ty2 * cos(heading)

    
    '''player's centre location dot'''
    pygame.draw.rect(display, red, (b2x+b2w/2 -1, b2y+b2h/2, 3, 3), 0)

    '''line coming out of the player, showing playa heading'''
    pygame.draw.line(display, blue, (b2x+b2w/2, b2y+b2h/2), (b2x+b2w/2, b2y+b2h/2 - 10), 1)

    '''this is a line'''
    pygame.draw.line(display, red, ((b2x + vx1) -tx1, (b2y + vy1) - tz1), ((b2x + vx2 )- tx2, (b2y + vy2) -tz2), 2)

    '''draw window enclosing box'''
    pygame.draw.rect(display, green, (b2x,b2y,b2w,b2h), boundarythickness)

    '''process eventz'''
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    quit()

    '''control key inputz'''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        px += cos(heading)
        py += sin(heading)
        
    elif keys[pygame.K_DOWN]:
        px -= cos(heading)
        py -= sin(heading)
        
    if keys[pygame.K_LEFT]:
        heading -= 0.1

    elif keys[pygame.K_RIGHT]:
        heading += 0.1

        
    '''Here's the window's boundary box collision rules'''
    if px <= boundarythickness:
        px = boundarythickness
    if py <= boundarythickness:
        py = boundarythickness
    if px >= 200 -boundarythickness:
        px = 200 - boundarythickness
    if py >= 200 - boundarythickness:
        py = 200 - boundarythickness
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
