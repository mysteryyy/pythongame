from item.item import Item
class ItemHandler:
    
    #List of items
    items = []

    def __init__(self):
        pass
    
    def setup(self):
        #Create items
        tv = Item("TV", "an internet-enabled smartTV", -10, 4)
        laptop = Item("Laptop", "a modern personal computer", -8, 6)
        phone = Item("MobilePhone", "a modern model of Android mobile", -6, 6)
        car = Item("Car", "A luxury car", -80, 15)
        villa = Item("Villa", "A villa is a fancy vacation home", -250, 25) 
        clothes = Item("Clothes", "You have to buy clothes every 7 days", -3, 2)
        shoes = Item("Shoes", "You have to buy shoes every 25 days", -5, 3)
        vitamin = Item("Vitamin", "promotes energy growth", -3, 8)
        pizza = Item("Pizza", "the pizza  is sold in Pizzeria", -4, 7)
        meal = Item("Meal", "A dish that can be purchased at Brasseria", -8, 10) 
        
        #Create services
        rest = Item("Rest", "have a rest at home", 0, 12) 
        work = Item("Work", "you are working as a sofware developer", 10, -12)
        knowledge = Item("Knowledge", "studying at the university will increase your monthly salary by 100 percent", -35, -20)

        self.items.append(tv)
        self.items.append(laptop)
        self.items.append(phone)
        self.items.append(car)
        self.items.append(villa)
        self.items.append(clothes)
        self.items.append(shoes)
        self.items.append(vitamin)
        self.items.append(pizza)
        self.items.append(meal)
  
        self.items.append(rest)
        self.items.append(work)  
        self.items.append(knowledge)          


    def get_items(self):
        return self.items

    def get_item(self, name):
        foundornot=False
        for item in self.items:
            if(item.name==name):
                foundornot=True
                return item
        if(not foundornot):
            return None
        
