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
game_over= False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.draw.rect(dis,orangecolor,[200,150,snake_block,snake_block])
    pygame.display.update()
pygame.quit()
quit()
