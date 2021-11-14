from characters.character import Character

class Player(Character):
    def __init__(self, name, items, min_value, min_energy):
        Character.__init__(self, name, items,min_value,min_energy)
        self.min_value = min_value
        self.min_energy = min_energy
        self.name=name
        self.items=items
    
    def get_min_value(self):
        return self.min_value

    def set_min_value(self, min_value):
        self.min_value = min_value
        
    def get_min_energy(self):
        return self.min_energy

    def set_min_energy(self, min_energy):
        self.min_energy = min_energy