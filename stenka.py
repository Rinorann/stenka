import pygame as pg
from raketka import Raketka
from ball import Ball
from target import Target
pg.init()
screen = pg.display.set_mode((1196, 610))
FINISH = False
FPS = 60
f1 = pg.font.Font(None, 36)
f2 = pg.font.Font(None, 36)

r = Raketka(screen)

b = Ball(screen)

t = Target(screen)
clock = pg.time.Clock()

pg.display.update()

TOTAL = 0
max = 0
while not FINISH:
    screen.fill('black')
    '''Табло с очками'''

    text1 = f1.render(str(TOTAL), True, (255, 255, 255))
    screen.blit(text1, (598, 305))

    '''Максимум'''
    if TOTAL > max:
        max = TOTAL
    text2 = f2.render(str(max), True, (255, 255, 255))
    screen.blit(text2, (1000, 100))


    r.draw()

    '''Работа мячика'''
    b.draw()
    b.motion()
            
    
    
    '''Цель'''
    t.draw() 
        

    pg.display.update()
    clock.tick(FPS)
    for event in pg.event.get():    
        if event.type == pg.QUIT:
            FINISH = True
        if event.type == pg.MOUSEMOTION:
            r.motion(event)                    
    pg.display.update()    
pg.quit()
