class Aviary():
    birds_list = []

    @classmethod
    def add_to_birds_list(cls, bird):
        cls.birds_list.append(bird)
        print(f"{bird} has been added to the list")

    def __init__(self, birds):
        self.add_to_birds_list(birds)

    def __str__(self):
        return f"Name: {self.name}\n Species: {self.species}\n"