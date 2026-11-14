import numpy as np
import pygame as game

H, W = 5, 5
scale = 100

palette = [(0, 0, 0)]*32

for x in range(32):
    if x<11 and x>0:
        palette[x] = (255/x, 0, 0)
    if x<21 and x>10:
        palette[x] = (255, (255/x)-10, 0)
    if x<31 and x>20:
        palette[x] = (255, 255, (255/x)-20)
palette[31] = (255, 255, 255)
palette[0] = (0, 0, 0)

game.init()

screen = game.display.set_mode((W*scale, H*scale))
game.display.set_caption('ETTI fire')

clock = game.time.Clock()

raster = game.Surface((W, H))
raster.fill((0, 0, 0))

running = True
while running:
    for event in game.event.get():
        if event.type==game.QUIT:
            running = False
        elif event.type==game.KEYDOWN:
            if event.key == game.K_c:
                raster.fill((0, 0, 0))
            if event.key == game.K_s:
                game.image.save(raster, 'fire.png')

    buttons = game.mouse.get_pressed()
    if buttons[0] or buttons[2]:
        mx, my = game.mouse.get_pos()
        x, y = mx // scale, my // scale
        if 0 <= x < W and 0 <= y < H:
            raster.set_at((x, y), palette[0] if buttons[2] else palette[31])

    big = game.transform.scale(raster, (W*scale,H*scale))
    screen.blit(big, (0, 0))
    game.display.flip()
    clock.tick(60)

game.quit()