import pygame
import sys
import random
import time
from lattice import Lattice
from popup import Popup
# 格子属性
width, height = 600, 600
single = width/3 - 1

# 判断胜负，当为1时电脑获胜，为-1个人获胜
judge = 0

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('井字棋')

# 表示九个格子
rect = [0]*9
rect_wh = [
    (1,1), (single+3,1), (single*2+5,1), 
    (1,single+3), (single+3,single+3), (single*2+5,single+3),
    (1,single*2+5), (single+3,single*2+5), (single*2+5,single*2+5)
    ]
for i in range(len(rect)):
    rect[i] = pygame.Rect(*rect_wh[i],single,single)
    rect[i] = Lattice(rect[i],screen)

def update(time_sleep=0,msg=""):
    screen.fill((255,228,181))
    for i in rect:
        pygame.draw.rect(screen,(255, 255, 255),i.rect)
        i.draw()
    if msg:
        Popup(screen,msg)
    pygame.display.flip()
    if time_sleep:
        time.sleep(time_sleep)

def computer():
    """电脑的回合，随机生成一个位置"""
    global judge
    random_num = [i for i in range(len(rect)) if not rect[i].stats]
    # 没位子下了，平局
    if not random_num:
        update(3,"draw")
        exit()
    rect[random.choice(random_num)].stats = 1

def win_or_lose():
    global judge
    stats1 = [i for i in range(len(rect)) if rect[i].stats == 1]
    stats2 = [i for i in range(len(rect)) if rect[i].stats == -1]
    win_list = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for i in win_list:
        if i == [j for j in i if j in stats1]:
            update(3,"Computer win!")
            exit()
        elif i == [j for j in i if j in stats2]:
            update(3,"You win!")
            exit()

def first_hand():
    """判断先手，如果随机数为1，则电脑先手"""
    x = random.randint(0,1)
    if x:
        x = random.randint(0,8)
        rect[x].stats = 1

# 游戏主体部分
first_hand()
while not judge:
    update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 判断玩家是否点击成功
            success = 0
            for i in rect:
                # 确定玩家下了一步
                if  not i.stats and i.rect.collidepoint(mouse_x,mouse_y):
                    success = 1
                    # 玩家下棋
                    i.stats = -1
                    update()
                    win_or_lose()
                    # 电脑下棋
                    update(0.3,"Computer choice!")
                    computer()
                    update()
                    win_or_lose()
                    update(0.3,"your choice!")

            if not success:
                update(0.3,"you can't choose here!")
