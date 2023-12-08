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
        for x in range(self.grid_size[0]):
            for y in range(self.grid_size[1]):
                tile = Tile(self.get_tile_width(), self.get_tile_height() , x , y)
                tile.draw_tile(self.screen, 'purple')
                tile.draw_lines(self.screen, 'white')
                self.grid.append(tile)

    def search_in_grid(self):
        for tile in self.grid:
            print("Width: ", tile.width,
                   "Height: ", tile.height,
                    "Cordinates: ", tile.cordinates)
    
    def search_in_grid_by_cordinates(self, user_cords):
        for tile in self.grid:
            if tile.cordinates == user_cords:
                
                return tile

    def get_tile_width(self):
        return self.width//self.grid_size[0]
    
    def get_tile_height(self):
        return self.height// self.grid_size[1]
    
    def get_tile_from_mouse_click(self,pos,button):
        print("Botonete: ", button)
        tiles_tuple = ( int(pos[0]/ self.get_tile_width()) , int(pos[1]/ self.get_tile_height()))
        

        tile = self.search_in_grid_by_cordinates(tiles_tuple)
        
        if button == 1:
            tile.draw_tile(self.screen, 'white')
        elif button == 3:
            tile.draw_tile(self.screen, 'red')



        return tiles_tuple




    

        



    

        


    
        



    

        