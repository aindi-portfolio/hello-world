class ReptileEnclosure():
    reptiles_list = []

    @classmethod
    def add_to_reptiles_list(cls, reptile):
        cls.reptiles_list.append(reptile)
        print(f"{reptile} has been added to the list")

    def __init__(self, reptile):
        self.add_to_reptiles_list(reptile)

x = ReptileEnclosure('snake')