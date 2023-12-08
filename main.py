import pygame
from Screen import Screen

pygame.init()

screen = Screen(400,720)
screen.draw_screen()
screen.draw_grid()

screen.search_in_grid()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit



    pygame.display.flip()  
    clock.tick(60)         