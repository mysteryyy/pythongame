import random

class Character:
    def __init__(self, name, items,value,energy):
        self.name = name
        self.items = items
        self.value = value
        self.energy = energy 
    
    def get_name(self):
        return self.name

    def move(self):
        exits = []
        for exit in self.get_room().get_exits():
            if self.get_room().get_exits()[exit] is not None:
                exits.append(exit)

        random_direction = random.choice(list(exits))

        self.get_room().remove_character(self)
        self.set_room(self.get_room().get_exit(random_direction))
        self.get_room().add_character(self)

    def set_name(self, name):
        self.name = name

    def get_items(self):
        return self.items
    
    def get_item_string(self):
        item_string = ""
        for item in self.items:
            item_string += "[" + item.get_name() + ", " + str(item.get_value()) + "]" + ", " \
                    + 'energy '+str(item.get_energy())
        item_string = item_string.strip(", ")
        return item_string

    def get_item(self, item_name):
        return next((item for item in self.items if item.name == item_name), None)

    def set_items(self, items):
        self.items = items

    def get_room(self):
        return self.room

    def set_room(self, room):
        self.room = room

    def pickup_item(self, item_name):
        self.items.append(item_name)

    def drop_item(self, item_name):
        for item in self.items:
            if item.get_name() == item_name:
                self.items.remove(item)
    
    def get_value(self):
        return self.value

    def set_value(self):
        #self.value = 0
        item=self.items[-1]
        self.value += item.get_value()
        #for item in self.items:
        #    self.value -= item.get_value()
        
    def get_energy(self):
        return self.energy

    def set_energy(self):
        #self.energy = 0
        #for item in self.items:
        #    self.energy += item.get_energy()
        item=self.items[-1]
        self.energy += item.get_energy()
