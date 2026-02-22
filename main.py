import pygame
from frontend.stage import stagedraw
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("My Game")

gamerun = True
while gamerun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerun = False
        
    screen.fill(("white"))
    stagedraw.center = (250, 250)
    pygame.draw.rect(screen,"ivory",stagedraw)
    pygame.display.flip()

pygame.quit()