import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

debugjump = 1
debugspeed = 1

x1 = list(range(0, 11))
y1 = [10] * 11

fig, ax = plt.subplots()
plot, = ax.plot(x1, y1)
plt.ylabel('Value')
plt.subplots_adjust(left=0.1, bottom=0.35)
plt.title("Debug options")
plt.axis([1, 10, 0, 100])

axslider1 = plt.axes([0.1, 0.2, 0.8, 0.05])
axslider2 = plt.axes([0.1, 0.1, 0.8, 0.05])
slider = Slider(axslider1, "Speed", valmin=0, valmax=10, valinit=1, valstep=0.1)
slider2 = Slider(axslider2, "Jump boost", valmin=0, valmax=10, valinit=1, valstep=0.1)


def val_update(val):
    yval = slider.val
    plot.set_ydata(yval)
    plt.draw()
slider.on_changed(val_update)
######################
import pygame
import easygui
pygame.init()

screenw = 500
screenh = 500

win = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("Game")




standj = 60

jumping = False
neg = 1
x = 50
y = 200
w = 60
h = 60

vel = 16

isJump = False


fallspeed = 0

render = 1
speed = (render/60)*vel
jumpCount = (render/60)*-standj
run = True
while run:
    pygame.time.delay(render)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and jumping == False:
        isJump = True

    if isJump == True:
        if jumpCount <= (render/60)*standj:
            y += (render/60)*jumpCount*standj*debugjump
            jumpCount += ((render/6)** 2) * 0.2
            print(str(y))
        else:
            isJump = False
            jumpCount = (render/60)*-standj

    else:
        if y <= screenh - 100:
            y += (render/60)*(fallspeed ** 1.3)
            fallspeed += 0.2
        else:
            fallspeed = 0



    if keys[pygame.K_a] and x > 0:
        x -= speed * debugspeed

    if keys[pygame.K_d] and x < screenw - w:
        x += speed * debugspeed

    if keys[pygame.K_ESCAPE]:
        plt.show()
        debugspeed = slider.val
        debugjump = slider2.val
    pygame.draw.rect(win, (0, 0, 0), (0, screenh - 50, screenw, 50))

    pygame.draw.rect(win, (255, 0, 0), (x, y, w, h))
    pygame.display.update()
    win.fill((0, 255, 0))

pygame.quit()