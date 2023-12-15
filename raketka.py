import pygame as pg
class Raketka:
    def __init__(self, screen, a = 300):
        '''инициализация'''
        self.screen = screen
        self.color = 'white'
        self.a = a 

    def draw(self):
        '''прорисовка'''
        pg.draw.rect(self.screen, self.color,  (100, self.a, 20, 100))

    def motion(self, event):
        '''движение относительно мыши'''
        self.a = event.pos[1]

    def restart(self):
        '''перезапуск'''
        self.a = 300