import pygame
import time
import random

pygame.init()
#declare colors
orangecolor=(255,123,7)
blackcolor=(0,0,0)
redcolor=(213,50,80)
greencolor=(0,255,0)
bluecolor=(50,153,213)

display_width=600
display_height=400
dis=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('snake game')
snake_block=10
snake_list=[]

#desfining the position of snake
def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,orangecolor,[200,150,snake_block,snake_block])


def snakegame():
    game_over= False
    game_end = False
    #co-ordinates
    x1 = display_width/2
    y1 = display_height/2
    #movements
    x1_change = 0
    y1_change = 0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.k_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
        if x1 >=display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True


        x1 += x1_change
        y1 += y1_change
        pygame.display.update()
    pygame.quit()
    quit()
