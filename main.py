import numpy as np
import pygame as game
import random

H, W = 256, 128                                   
scale = 3

wind = 1

palette = [(0, 0, 0)] * 32

for i in range(1, 11):                          
    palette[i] = (int(255 * i / 10), 0, 0)
for i in range(11, 21):                         
    palette[i] = (255, int(255 * (i - 10) / 10), 0)
for i in range(21, 31):                         
    palette[i] = (255, 255, int(255 * (i - 20) / 10))
palette[31] = (255, 255, 255)
palette[0] = (0, 0, 0)

game.init()

screen = game.display.set_mode((W * scale, H * scale))
game.display.set_caption('ETTI fire')

clock = game.time.Clock()

raster = game.Surface((W, H))
raster.fill((0, 0, 0))

kindle = np.dtype([
    ('temp', np.uint8)
])

fire = np.zeros((H, W), dtype=kindle)
temp = fire['temp']                             

source_on = True

def apply_source():
    temp[H - 1, :] = 31 if source_on else 0

def reset():
    temp[:] = 0
    apply_source()

def draw():
    for y in range(H-2, 0, -1):
        for x in range(W,-1 0, -1):
            rand = random.randrange(0, 2, 1)
            dt = int(temp[y+1, x])-rand
            if dt<0:
                dt=0
            if x-rand < 0:
                temp[y, x] = dt
            else:
                temp[y, x-rand*wind] = dt

    for y in range(H):                          
        for x in range(W):
            raster.set_at((x, y), palette[temp[y, x]])

reset()

running = True
while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        elif event.type == game.KEYDOWN:
            if event.key == game.K_c:
                reset()
            if event.key == game.K_s:
                game.image.save(raster, 'fire.png')
        elif event.type == game.MOUSEBUTTONDOWN and event.button == 2:
            source_on = not source_on
            apply_source()

    buttons = game.mouse.get_pressed()
    if buttons[0] or buttons[2]:
        mx, my = game.mouse.get_pos()
        x, y = mx // scale, my // scale
        if 0 <= x < W and 0 <= y < H:
            temp[y, x] = 0 if buttons[2] else 31   

    draw()

    big = game.transform.scale(raster, (W * scale, H * scale))
    screen.blit(big, (0, 0))
    game.display.flip()
    clock.tick(24)

game.quit()