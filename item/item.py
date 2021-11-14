class Item:
    def __init__(self, name, description, value, energy):
        self.name = name
        self.description = description
        self.value = value
        self.energy=energy

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

    def get_energy(self):
        return self.energy
    