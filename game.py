from random import randint
from snake import Snake
import pygame
from pygame.locals import *
from food import Food

scale = 5
size = 800

def findEmptySpace(snake):
    x,y = randint(0,(size/scale**2)-1)*scale,randint(0,(size/scale**2)-1)*scale
    if not snake.isInBody(x, y):
        return [x, y]
    return findEmptySpace(snake)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((size, size),SCALED)
pygame.display.set_caption('Snake')
screen.fill(0)
snek = Snake()
food = Food(findEmptySpace(snek))
pygame.draw.rect(screen, (255, 0, 0), (snek.head[0]*scale, snek.head[1]*scale, scale, scale))
font = pygame.font.Font('freesansbold.ttf', 32)
# text = font.render('Game over', True, green, ())

run = True
while run:
    clock.tick(5)
    # print(snek.body)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        elif event.type == KEYDOWN:
            if event.key == pygame.K_q:
                run = False
            elif event.key == pygame.K_g:
                snek.grow()
            elif event.key == K_RIGHT:
                snek.turn('right')
            elif event.key == K_LEFT:
                snek.turn('left')
            elif event.key == K_UP:
                snek.turn('up')
            elif event.key == K_DOWN:
                snek.turn('down')
    snek.move()
    if snek.isInBody(snek.head):
        run = False
    screen.fill(0)
    pygame.draw.rect(screen, (255, 0, 0), (snek.head[0]*scale, snek.head[1]*scale, snek.scale, snek.scale))
    for i in range(len(snek.body)):
        pygame.draw.rect(screen, (255, 0, 0), (snek.body[i][0]*scale, snek.body[i][1]*scale, snek.scale, snek.scale))
    # draw food if not eaten
    if snek.isEating(food):
        food = Food(findEmptySpace(snek))
    else:
        pygame.draw.rect(screen, (0, 255, 0), (food.position[0]*scale, food.position[1]*scale, 25, 25))
    pygame.display.update()