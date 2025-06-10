import re

class Student:
    def __init__(self, name, age=13, grade="12th"):
        self.name = name
        self.age = age
        self.grade = grade

    #Getter for name attribute
    @property
    def name(self):
        return self._name
    
    #Setter for name attribute
    @name.setter
    def name(self, new_name: str) -> None:
        new_name = new_name.strip()
        if (len(new_name) >= 3 and new_name.isalnum() and new_name.title() == new_name):
            self._name = new_name
        else:
            print("Name input is in incorrect format")

    def __str__(self):
        return f"Student 1: Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

aindi = Student('  Aindi  ')

print(aindi.__str__())