import pygame as pg
from raketka import Raketka
from ball import Ball
from target import Target


class Game:

    def __init__(self):    
        pg.init()
        self.screen = pg.display.set_mode((1196, 610))
        self.FINISH = False
        self.FPS = 60
        self.f1 = pg.font.Font(None, 36)
        self.f2 = pg.font.Font(None, 36)

        self.r = Raketka(self.screen)
        self.b = Ball(self.screen)
        self.t = Target(self.screen)
        self.clock = pg.time.Clock()
        pg.display.update()
        self.TOTAL = 0
        self.max = 0


    def draw_table(self):
        '''Табло с очками'''
        text1 = self.f1.render(str(self.TOTAL), True, (255, 255, 255))
        self.screen.blit(text1, (598, 305))
        '''Максимум'''
        if self.TOTAL > self.max:
            self.max = self.TOTAL
        text2 = self.f2.render(str(self.max), True, (255, 255, 255))
        self.screen.blit(text2, (1000, 100))

    def run(self):
        FINISH = False
        while not FINISH:
            self.screen.fill('black')
            self.draw_table()

            self.r.draw()

            '''Работа мячика'''
            self.b.draw()
            self.b.motion()
            self.b.collapse_from_wall()
            self.b.collapse_from_raketka(self.r, self)
            self.b.restart(self)
            self.b.hittest(self.t)
                
            
            '''Цель'''
            self.t.draw()
            self.t.restart(self.b, self) 

            pg.display.update()
            self.clock.tick(self.FPS)
            for event in pg.event.get():    
                if event.type == pg.QUIT:
                    FINISH = True
                if event.type == pg.MOUSEMOTION:
                    self.r.motion(event)                    
            pg.display.update()    

    def close():
        pg.quit()
