import pygame
import math
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


pygame.init()
screen = pygame.display.set_mode([900, 900])
pygame.display.set_caption('Rocket Solvers!')
running = True
screen.fill(white)
while running:
    screen.fill(red)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
            


    
