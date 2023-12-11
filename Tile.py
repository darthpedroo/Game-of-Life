import pygame

class Tile():
    def __init__(self, width, height, x_cordinate, y_cordinate):
        self.width = width
        self.height = height
        self.cordinates = (x_cordinate, y_cordinate)
        self.is_alive = False
        self.colors = {'background' : 'black', 'alive' : 'white', 'dead': 'black'}
    
    def draw_tile(self,screen,color):
        pygame.draw.rect(screen, color, pygame.Rect(self.cordinates[0] * self.width , self.cordinates[1] * self.height, self.width, self.height)) # X , Y , WIDTH , HEIGTH

    def draw_lines(self,screen,color):
        pygame.draw.rect(screen, color, pygame.Rect(self.cordinates[0] * self.width , self.cordinates[1] * self.height, 1, self.height))
        pygame.draw.rect(screen, color, pygame.Rect(self.cordinates[0] * self.width , self.cordinates[1]  * self.height -1, self.width, 1))
    
    def set_alive_state(self, screen ,state, color):
        self.is_alive = state
        self.draw_tile(screen, self.colors[color]) #Cambiar esto, redibujar el grid cuando se actualizan todos.
    


    
    
    
    



        