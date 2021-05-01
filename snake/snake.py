""""🐍类"""
import pygame
class Snake():
    def __init__(self,snake_color,snake_head_color,x,y,lattice_wh):
        self.color = snake_color
        self.head_color = snake_head_color
        # 格子的左上角坐标
        self.pos = (x,y)
        self.lattice_wh = lattice_wh
        self.rect = pygame.Rect(x,y,self.lattice_wh,self.lattice_wh)

        self.move_distance = {
            0:(0,0),
            1:(0,-self.lattice_wh),
            2:(0, self.lattice_wh),
            3:(-self.lattice_wh,0),
            4:( self.lattice_wh,0)
        }
    
    def move(self,direction):
        self.rect.x += self.move_distance[direction][0]
        self.rect.y += self.move_distance[direction][1]
    
    def forecast(self,direction):
        return (self.rect.x+self.move_distance[direction][0],self.rect.y+self.move_distance[direction][1])