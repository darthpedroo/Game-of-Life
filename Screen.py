import pygame
from Tile import Tile

class Screen():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = None
        self.grid_size = [10,10]
        self.grid = [] #This is the list with the objects
        self.new_neighbours = [] #Hacer algo para que cheke el grid pero no lo "borre", sino que lo mande a otra lista, de ahí, que redibuje el grid y haga lo mismo.
        self.colors = {'background' : 'black', 'alive' : 'white', 'dead': 'black'}

    def draw_screen(self):
        self.screen = pygame.display.set_mode((self.width,self.height))
    
    def draw_grid(self):
        for x in range(self.grid_size[0]):
            for y in range(self.grid_size[1]):
                tile = Tile(self.get_tile_width(), self.get_tile_height() , x , y)
                tile.draw_tile(self.screen, self.colors['background'])
                tile.draw_lines(self.screen, 'white')
                self.grid.append(tile)

    def search_in_grid(self):
        for tile in self.grid:
            print("Width: ", tile.width,
                   "Height: ", tile.height,
                    "Cordinates: ", tile.cordinates,
                    "Is Alive: ", tile.is_alive)
    
    #Hay que hacer un algoritmo que, dadas las cordenadas, devuelva si los vecinos estan vivos o muertos y dependiendo de eso vive o muere. 
    
    def check_neighbours_alive(self):
        for tile in self.grid:
            cordinates = tile.cordinates
            counter = 0
            for tile_2 in self.grid:
                # Checkear la que esta a la izquierda y la que está a la derecha
                if ( (tile_2.cordinates == (cordinates[0] -1, cordinates[1]))  or (tile_2.cordinates == (cordinates[0] +1, cordinates[1])) ):
                    if tile_2.is_alive:
                        counter +=1
                # Checkear arriba y abajo 

                if ( (tile_2.cordinates == (cordinates[0] , cordinates[1]-1))  or (tile_2.cordinates == (cordinates[0] , cordinates[1] +1)) ):
                    if tile_2.is_alive:
                        counter +=1
                #Checkear Diagonales
                if (

                    (tile_2.cordinates == ( cordinates[0]-1, cordinates[1]+1)) or
                    (tile_2.cordinates == (cordinates[0] -1, cordinates[1] -1 )) or
                    (tile_2.cordinates == (cordinates[0] +1, cordinates[1] -1 )) or
                    (tile_2.cordinates == (cordinates[0] +1, cordinates[1] +1 ))
                ):
                    if tile_2.is_alive:
                        counter +=1
            
            if tile.is_alive:
                if counter < 2:
                    tile.set_alive_state(self.screen, False,'dead')
                elif counter > 2 and counter <= 3:
                    tile.set_alive_state(self.screen,True,'alive')
                elif counter > 3:
                    tile.set_alive_state(self.screen,False,'dead')
            else:
                if counter == 3:
                    tile.set_alive_state(self.screen,True,'alive')

            #self.search_in_grid()
        

    def search_in_grid_by_cordinates(self, user_cords):
        for tile in self.grid:
            if tile.cordinates == user_cords:
                
                return tile

    def get_tile_width(self):
        return self.width//self.grid_size[0]
    
    def get_tile_height(self):
        return self.height// self.grid_size[1]
    
    def get_tile_from_mouse_click(self,pos,button):
        #print("Botonete: ", button)
        tiles_tuple = ( int(pos[0]/ self.get_tile_width()) , int(pos[1]/ self.get_tile_height()))
        

        tile = self.search_in_grid_by_cordinates(tiles_tuple)
        
        if button == 1:
            is_alive = True
            tile.set_alive_state(self.screen, is_alive,'alive')
        elif button == 3 :
            is_alive = False
            tile.set_alive_state(self.screen, is_alive,'dead')
        elif button == 4:
            self.check_neighbours_alive()

        

        #self.search_in_grid()
        

        #Fix the "Draw Lines"

        return tiles_tuple




    

        



    

        


    
        



    

        