class Field:

    def __init__(self):
        self.homeless_coordinates = {}
            
    def add_homeless(self, homeclass Coordenada:
        
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)
    
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y
        
        self.homeless_coordinates[homeless] = coordinate
        
    def move_homeless(self, homeless):
        delta_x, delta_y = homeless.walk()
        current_coordinate = self.homeless_coordinates[homeless]
        new_coordinate = current_coordinate.move(delta_x, delta_y)
        self.homeless_coordinates[homeless] = new_coordinate
        
    def get_coordinate(self, homeless):
        return self.homeless_coordinates[homeless]