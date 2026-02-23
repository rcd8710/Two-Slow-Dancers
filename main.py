from frontend.dancers import dancer1,dancer2
import pygame


pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Two slow dancer")
clock = pygame.time.Clock()
gamerun = True
while gamerun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerun = False
        
    screen.fill(("white"))
    
    pygame.draw.rect(screen,"ivory", (0,0,499,499))
    dancer1.drawDancer(screen)
    dancer2.drawDancer(screen)
    dancer1.mirror()
    dancer2.mirror()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()