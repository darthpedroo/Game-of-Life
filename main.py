import pygame
from Screen import Screen

pygame.init()

screen = Screen(1000,680)
screen.draw_screen()
screen.draw_grid()

#screen.search_in_grid()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:

            pos = pygame.mouse.get_pos()
            screen.get_tile_from_mouse_click(pos, event.button)
    
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.flip()  
    clock.tick(60)         