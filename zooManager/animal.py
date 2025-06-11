class Animal:
    def __init__(self, name:str, species:str):
        self.name = name
        self.species = species

    def speak(self, sound):
        return f"The animal makes the {sound} sound."