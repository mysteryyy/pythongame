from room.room import Room
from item.item import Item
from characters.character import Character
from handlers.characterhandler import CharacterHandler

class RoomHandler:
    
    rooms = []

    def __init__(self, item_handler, character_handler):
        self.characters = character_handler
        self.items = item_handler
    
    def setup(self):
        #Create rooms
        
        home = Room("House", '''a home where \ 
                you can get 12 units of \
                energy without spending money. However, \
                you can enter home only in the evening to \ 
                have a rest and leaving will be a NEW DAY.\ 
                You have to use Pizza or Brasserie services\
                before coming house every day''', {}, [self.characters.get_player()], [])
        yard = Room("Yard", "courtyard with a fountain in the center.", {}, [self.characters.get_character("Rapunzel")],[])
        market = Room("Market", "a place where you can buy TV, laptop, mobilephone, car and villa TO WIN THE GAME.", {}, [self.characters.get_character("Rocky")], [self.items.get_item("TV"), self.items.get_item("Laptop"), self.items.get_item("MobilePhone"), self.items.get_item("Car"), self.items.get_item("Villa")])
        university = Room("University", "You can increase your monthly salary up to 100% by using university services.", {}, [self.characters.get_character("Morgana")], [self.items.get_item("Knowledge")])
        sidewalk = Room("Sidewalk", "the sidewalk leading to the office and cityMall.", {}, [self.characters.get_character("Rapunzel")],[])
        office = Room("Office", "the only place where you can earn money.",{}, [self.characters.get_character("Bob")],[self.items.get_item("Work")])
        hall = Room("Hall", "Entrance part of CityMall on the groundfloor. From here you can access various eateries or go to the first floor.", {}, [self.characters.get_character("Bob"), self.characters.get_character("Lofty")],[])
        pizzeria = Room("Pizzeria", "You can eat different pizzas here.", {}, [self.characters.get_character("Rapunzel")],[self.items.get_item("Pizza")])
        brasserie = Room("Brasserie", "a French style restaurant.", {}, [self.characters.get_character("Rocky")], [self.items.get_item("Meal")])
        uphall = Room("Uphall", "first floor hall of CityMall. You can access to shop and pharmacy.", {}, [self.characters.get_character("Morgana")], [])
        pharm = Room("Pharmacy ", "It is recommended to take no more than 1 vitamin per day to get more energy.", {}, [], [self.items.get_item("Vitamin")])
        shop = Room("Shop", "a store where you can buy clothes and shoes. You will need to buy clothes after 7 days and shoes after 25 days.", {}, [], [self.items.get_item("Clothes"), self.items.get_item("Shoes")])

        #Create exits
        home.set_exits({"north" : None, "east" : None, "south" : None, "west" : yard})
        yard.set_exits({"north" : sidewalk, "east" : home, "south" : market, "west" : university})
        university.set_exits({"north" : None, "east" : yard, "south" : None, "west" : None})
        market.set_exits({"north" : yard, "east" : None, "south" : None, "west" : None})
        sidewalk.set_exits({"north" : hall, "east" : None, "south" : yard, "west" : office})
        office.set_exits({"north" : None, "east" : sidewalk, "south" : None, "west" : None})
        hall.set_exits({"upstairs" : uphall , "east" : pizzeria, "south" : sidewalk, "west" : brasserie})
        pizzeria.set_exits({"north" : None, "east" : None, "south" : None, "west" : hall})
        brasserie.set_exits({"north" : None, "east" : hall, "south" : None, "west" : None})
        uphall.set_exits({"downstairs" : hall, "east" : shop, "south" : None, "west" : pharm})
        pharm.set_exits({"north" : None, "east" : uphall, "south" : None, "west" : None})
        shop.set_exits({"north" : None, "east" : None, "south" : None, "west" : uphall})

        self.characters.get_player().set_room(home)
        self.characters.get_character("Bob").set_room(university)
        
        self.characters.get_character("Lofty").set_room(home)
        self.characters.get_character("Rapunzel").set_room(shop)
        self.characters.get_character("Rocky").set_room(pizzeria)
        self.characters.get_character("Morgana").set_room(hall)
        self.characters.get_character("James").set_room(pharm)

    def get_rooms(self):
        return self.rooms

    def get_room(self, name):
        for room in self.rooms: 
            if room.name == name:
                return room
    
    def get_character_handler(self):
        return self.characters
