from random import randint, random
import pygame as pg

class Ball():
    def __init__(self, screen, x=randint(500, 800), y=randint(1, 610)):
        '''конструктор'''
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 10
        self.vy = 10
        self.tan = random()
               
    def turn(self):
        '''поворот при отталкивании'''
        self.tan = random()    
        
    def draw(self):
        '''прорисовка'''
        pg.draw.circle(self.screen, 'white', (self.x, self.y), self.r)

    def motion(self):
        '''расчёт движения'''
        self.x += self.vx
        self.y += self.vy * self.tan
    
    def restart(self, game):
        '''рестарт'''
        if self.x <= 110:
            self.x = randint(300, 1000)
            self.y = randint(1, 610)
            game.TOTAL = 0
    
    def hittest(self, target):
        """Функция проверяет сталкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if abs((self.x - target.x)**2 + (self.y - target.y)**2 - (target.r + self.r)**2) < 100:
            return True           
        else:
            return False
        
    def collapse_from_raketka(self, roket, game):
        '''отталкивание от ракетки'''
        if self.x - self.r <= 120 and roket.a <= self.y <= roket.a + 100: # условие отталкивания от ракетки
            self.turn()
            self.vx = -self.vx
            self.vy = -self.vy
            game.TOTAL += 1
        
            
    def collapse_from_wall(self):
        '''отталкивание от стенки'''
        if self.x >= 1196: #отталкивание от стен
            self.vx = -self.vx
            self.turn()          
        if self.y >= 610 or self.y <= 0:  # отталкивание от стен
            self.vy = -self.vy
            self.turn()
            
    