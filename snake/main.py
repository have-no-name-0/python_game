import pygame
from fuc import *
from snake import Snake
from time import sleep
from food import Food
# 基本属性
lattice_wh = 20 #长宽
snake_color = (84, 255, 159)
snake_head_color = (123, 104, 238)
food_color = (255, 64, 64)

# 绘制界面
pygame.init()
screen = pygame.display.set_mode((25*lattice_wh,25*lattice_wh))
pygame.display.set_caption('贪吃蛇')

# 设置帧率
FPS=10
level = 0.9     # 每吃掉一个，间隔时间缩短系数
FPSClock=pygame.time.Clock()

if_lose = 1
if_food = 1

# 蛇的方向
direction = 0
# 得分，吃一个一分
num = 0

# 蛇头&1个蛇身
snakes = []
snakes.append(Snake(snake_color,snake_head_color,lattice_wh,24*lattice_wh,lattice_wh))
snakes.append(Snake(snake_color,snake_head_color,0,24*lattice_wh,lattice_wh))

# 食物
food = create_food(food_color,screen,lattice_wh,snakes)

# 游戏状态打包
game_stats =[if_lose,direction,num,food]

# 方向冲突
conflict = {
    pygame.K_RIGHT:4,
    pygame.K_LEFT :3,
    pygame.K_UP   :1,
    pygame.K_DOWN :2,
    0:0,
    1:2,
    2:1,
    3:4,
    4:3
}

while game_stats[0]:
    update(screen,lattice_wh,snakes,game_stats)
    check_events(game_stats,conflict,snakes,snake_color,snake_head_color,lattice_wh,food_color,screen)
    going(snakes,snake_color,snake_head_color,lattice_wh,game_stats,food_color,screen)
    FPSClock.tick(FPS* level**num)
