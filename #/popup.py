"""在游戏过程中，添加各种弹窗"""
import pygame
class Popup():
    def __init__(self, screen,msg):
        self.msg = msg
        self.screen = screen
        self.bg_color = (0, 0, 0)
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None,48)
        self.msg_image = self.font.render(msg,True,self.text_color,self.bg_color)
        self.msg_rect = self.msg_image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.msg_rect.center = self.screen_rect.center
        self.screen.blit(self.msg_image,self.msg_rect)
