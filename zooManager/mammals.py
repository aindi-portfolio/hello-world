from animal import Animal

class Mammal(Animal):
    # mammal_list = []

    # @classmethod
    # def add_to_mammal_list(cls, mammal):
    #     cls.mammal_list.append(mammal)
    #     print(f"{mammal} has been added to the list")

    def __init__(self, name, species):
        super().__init__(name, species)
        # self.add_to_mammal_list(self)

    def give_birth(self):
        return "The mammal has given birth."
    
    def __str__(self):
        return f"Name: {self.name}\n Species: {self.species}\n"
    
# dolphin = Mammal('Joey', 'Dolphin')
# elephant = Mammal('Po', 'Groundling')
