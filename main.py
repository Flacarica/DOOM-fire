import numpy as np
import pygame as game
import random

H, W = 64, 128                                   # (rânduri, coloane) - ordinea de la numpy
scale = 6

palette = [(0, 0, 0)] * 32

for i in range(1, 11):                          # negru -> rosu
    palette[i] = (int(255 * i / 10), 0, 0)
for i in range(11, 21):                         # rosu -> galben
    palette[i] = (255, int(255 * (i - 10) / 10), 0)
for i in range(21, 31):                         # galben -> alb
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
temp = fire['temp']                             # view 2D doar pe campul temp, ce scrii aici ajunge in fire

source_on = True

def apply_source():
    temp[H - 1, :] = 31 if source_on else 0

##
#
#   parcurg de sus in jos, exceptand cel mai de jos rand (sursa)
#
#   temperatura la coordonata resp va fi temperatura casetei de mai jos - rand(1,3)
#
##

def reset():
    temp[:] = 0
    apply_source()

def draw():
    for y in range(H - 1):                      # H-1 ca sa nu atingem sursa
        for x in range(W):
            dt = int(temp[y + 1, x]) - random.randrange(0, 3, 1)   # int() ca sa nu facem wraparound pe uint8
            temp[y, x] = dt if dt > 0 else 0

    for y in range(H):                          # desenam tot, inclusiv sursa
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
            temp[y, x] = 0 if buttons[2] else 31   # scriem in fire, nu direct in raster

    draw()

    big = game.transform.scale(raster, (W * scale, H * scale))
    screen.blit(big, (0, 0))
    game.display.flip()
    clock.tick(24)

game.quit()