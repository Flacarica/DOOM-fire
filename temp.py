import pygame                                                                                           #   importam belboteca pygame ca ne e lene sa ne facem noi 

W = H = 64                                                                                              #   definim dimensiunea rasterului
scale = 10                                                                                              #   cati pixeli irl inseamna un pixel din raster
                                                                                                        #   basically un scalar (asa cum ii zice si numele lmao)
palette = [(0, 0, 0)] *32

palette[0] = (0, 0, 0)                                                                                  #   aista-i negru
palette[31] = (255, 255, 255)                                                                           #   aista-i alb

for i in range(1, 11):
    palette[i] = (int(255*i / 10), 0, 0)

for i in range(11, 21):
    palette[i] = (255, int(255*(i-10) / 10), 0)

for i in range(21, 31):
    palette[i] = (255, 255, int(255*(i-20) / 10))

pygame.init()                                                                                           #   fakem init

screen = pygame.display.set_mode((W * scale, H * scale))                                                #   fereastra de dim W*scale x H*scale
pygame.display.set_caption('DOOM Fire')                                                                 #   cu titlu, ne permitem
                                                                                                        #poate schimb si imaginea din banner, who knows
                                                                                                        
clock = pygame.time.Clock()                                                                             #   generator de tick-uri ca sa am conceptu de frame

raster = pygame.Surface((W, H))                                                                         #   fac un raster de pixeli W x H
raster.fill((0, 0, 0))                                                                                  #   si il umplu cu negru

for x in range(H):
    raster.set_at((0, x), palette[x] if x < 32 else palette[x-32])                                      #   .set_at((vector coord xy), (vector culoare rgb fara canal de luma sau alpha cum drq se cheama))

running = True                                                                                          #   state-ul 
while running:                                                                                          #   main loop
    for event in pygame.event.get():                                                                    #   asta e event handler-ul
        if event.type == pygame.QUIT:                                                                   #   daca iesim, iesim
            running = False
        elif event.type == pygame.KEYDOWN:                                                              #   daca apasam
            if event.key == pygame.K_c:                                                                 #   nu merge, habar n-am, dar ar trebui sa stearga tot
                raster.fill((0, 0, 0))
            elif event.key == pygame.K_s:                                                               #   n-am testat, dar ar trebui sa salveze rasteru
                pygame.image.save(raster, 'raster.png')

    buttons = pygame.mouse.get_pressed()                                                                #   vector de stare pentru LClick si RClick
    if buttons[0] or buttons[2]:
        mx, my = pygame.mouse.get_pos()                                                                 #   daca [0] e LClick si [2] e RClick, oricare e apasat, stocam coordonata xy fara scalar
        x, y = mx // scale, my // scale
        if 0 <= x < W and 0 <= y < H:                                                                   #   daca suntem inca in raster
            raster.set_at((x, y), palette[5] if buttons[0] else (0, 0, 0))                              #   si daca apasam LClick, punem alb, daca RClick, punem negru

    big = pygame.transform.scale(raster, (W*scale, H*scale))                                            #   smre de stiu ce fac astea
    screen.blit(big, (0, 0))
    pygame.display.flip()
    clock.tick(60)                                                                                      #   le tick

pygame.quit()                                                                                           #   quit lmao