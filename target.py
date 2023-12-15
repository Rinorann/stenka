from random import randint, random
import pygame as pg

class Target():
    def __init__(self, screen, x=randint(900, 1000), y=randint(100, 500)):
        self.points = 0
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 20
        

    def draw(self): # прорисовка
        pg.draw.circle(self.screen, 'red', (self.x, self.y), self.r)
    
    def restart(self, ball, game):
        if ball.hittest(self):
            print('lol')
            self.x = randint(200, 1000) 
            self.y= randint(300, 400)
            game.TOTAL += 10
    
