from mammals import Mammal

class Marsupial(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def carry_baby(self):
        return f"{self} is carrying its baby."
    