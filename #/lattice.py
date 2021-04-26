import pygame
class Lattice():
    def __init__(self,rect,screen):
        self.rect = rect
        self.screen = screen
        # 0表示初始，1表示个人-1表示电脑
        self.stats = 0
        # 被选中的格子
        self.text_color = (30, 30, 30)
        self.bg_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None,48)

    def draw(self):
        # 按照状态显示
        msg = ""
        if self.stats == -1:
            msg = "x"
        elif self.stats == 1:
            msg = "o"
        
        if msg:
            self.msg_image = self.font.render(msg,True,self.text_color,self.bg_color)
            self.msg_rect = self.msg_image.get_rect()
            self.msg_rect.center = self.rect.center
            self.screen.blit(self.msg_image,self.msg_rect)