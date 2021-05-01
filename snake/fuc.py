import pygame
import sys
import time
from random import randint
from food import Food
from snake import Snake
"""存储了相关的函数"""
def update(screen,lattice_wh,snakes,game_stats):
    """屏幕刷新"""
    # 背景颜色
    screen.fill((255,255,255))
    # 画蛇，需要先画，不然网格会被盖住
    pygame.draw.rect(screen,snakes[0].head_color,snakes[0].rect)
    for i in range(1,len(snakes)):
        pygame.draw.rect(screen,snakes[i].color,snakes[i].rect)
    # 绘制网格
    for i in range(25):
        pygame.draw.line(screen,(105, 105, 105),(0,lattice_wh*i),(500,lattice_wh*i))
    for i in range(25):
        pygame.draw.line(screen,(105, 105, 105),(lattice_wh*i,0),(lattice_wh*i,500))
    # 绘制食物
    game_stats[3].draw()
    pygame.display.flip()

def check_events(game_stats,conflict,snakes,snake_color,snake_head_color,lattice_wh,food_color,screen):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in conflict:
                ret = conflict[event.key]
                if conflict[ret] != game_stats[1]:
                    game_stats[1] = ret
                    # going可以不要
                    # going(snakes,snake_color,snake_head_color,lattice_wh,game_stats,food_color,screen)
        elif event.type == pygame.QUIT:
            sys.exit()

def going(snakes,snake_color,snake_head_color,lattice_wh,game_stats,food_color,screen):
    """蛇的移动和转向问题"""
    if not game_stats[1]:
        return
    
    (x,y) = snakes[0].forecast(game_stats[1])
    # 撞到边界
    if x == -lattice_wh or x == 25*lattice_wh or y == -lattice_wh or y == 25*lattice_wh:
        game_stats[0] = 0
        return
    # 吃到食物
    if (x,y) == (game_stats[3].x,game_stats[3].y):
        head = Snake(snake_color,snake_head_color,x,y,lattice_wh)
        snakes.insert(0,head)
        game_stats[2] += 1
        game_stats[3] = create_food(food_color,screen,lattice_wh,snakes)
        return
    # 撞到蛇身
    for i in snakes:
        if (x,y) == (i.rect.x,i.rect.y):
            game_stats[0] = 0
            return
    for i in range(len(snakes)-1,0,-1):
        snakes[i].rect.x = snakes[i-1].rect.x
        snakes[i].rect.y = snakes[i-1].rect.y
    
    snakes[0].move(game_stats[1])
    
def create_food(food_color,screen,lattice_wh,snakes):
    success = 0
    x,y = 0,0
    while not success:
        x,y = randint(0,24),randint(0,24)
        x *= lattice_wh
        y *= lattice_wh
        for i in snakes:
            if (x,y) != (i.rect.x,i.rect.y):
                success = 1
                break
    food = Food(food_color,screen,lattice_wh,x,y)
    return food
    