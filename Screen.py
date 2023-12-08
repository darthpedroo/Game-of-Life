import pygame
from Tile import Tile

class Screen():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = None
        self.grid_size = [10,10]
        self.grid = [] #This is the list with the objects

    def draw_screen(self):
        self.screen = pygame.display.set_mode((self.width,self.height))
    
    def draw_grid(self):
        for x in range(self.grid_size[0]+10):
            for y in range(self.grid_size[1]+10):
                tile = Tile(self.set_tile_width(), self.set_tile_height() , x , y)
                tile.draw_tile(self.screen, 'purple')
                tile.draw_lines(self.screen, 'white')
                self.grid.append(tile)

    def search_in_grid(self):
        for tile in self.grid:
            print("Width: ", tile.width,
                   "Height: ", tile.height,
                    "Cordinates: ", tile.cordinates)

    def set_tile_width(self):
        return self.width//self.grid_size[0]
    
    def set_tile_height(self):
        return self.height// self.grid_size[1]


    

        


    
        



    

        