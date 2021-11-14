from characters.character import Character

class Npc(Character):
    def __init__(self, name, items, description,value,energy):
        Character.__init__(self, name, items,value,energy)
        self.description = description
        self.items=items
        self.value=value
        self.energy=energy
    
    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
        