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
pygame.draw.rect(screen, (255, 0, 0), (snek.head[0]*scale, snek.head[1]*scale, snek.size, snek.size))
font = pygame.font.Font('freesansbold.ttf', 128)

run = True
game_over = False
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
            elif event.key == K_RIGHT and (snek.direction != 'left' or snek.length == 0):
                snek.turn('right')
            elif event.key == K_LEFT and (snek.direction != 'right' or snek.length == 0):
                snek.turn('left')
            elif event.key == K_UP and (snek.direction != 'down' or snek.length == 0):
                snek.turn('up')
            elif event.key == K_DOWN and (snek.direction != 'up' or snek.length == 0):
                snek.turn('down')
    if not game_over:
        snek.move()
        if snek.isInBody(snek.head[0], snek.head[1]):
            game_over=True
        screen.fill(0)
        pygame.draw.rect(screen, (38, 38, 174), (snek.head[0]*scale, snek.head[1]*scale, snek.size, snek.size))
        for i in range(len(snek.body)):
            pygame.draw.rect(screen, (54, 54, 213), (snek.body[i][0]*scale, snek.body[i][1]*scale, snek.size, snek.size))
        # draw food if not eaten
        if snek.isEating(food):
            food = Food(findEmptySpace(snek))
            snek.grow()
        else:
            pygame.draw.rect(screen, (255, 0, 0), (food.position[0]*scale, food.position[1]*scale, snek.size, snek.size))
    else:
        screen.fill(0)
        text = font.render('Game over', True, (255, 0, 0), (255,255,0))
        screen.blit(text, (size/2-text.get_width()/2, size/2-text.get_height()/2))
    pygame.display.update()