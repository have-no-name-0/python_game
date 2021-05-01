"""食物类"""
import pygame
class Food():
    def __init__(self,food_color,screen,lattice_wh,x,y):
        self.screen = screen
        self.food_color = food_color
        self.lattice_wh = lattice_wh
        self.radius = lattice_wh/2
        self.x,self.y = x,y

    def draw(self):
        pos = (self.x+self.lattice_wh/2,self.y+self.lattice_wh/2)
        pygame.draw.circle(self.screen,self.food_color,pos,self.radius,int(self.radius))