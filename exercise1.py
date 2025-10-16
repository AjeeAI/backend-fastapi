class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        
    def display(self):
        print(f"The name of this pet is {self.name}. It is of the {self.species} species and it is {self.age} years old.")
        
    def celebrate_bd(self):
        print(f"Hurray!!! It's your birthday {self.name}")
        


dog = Pet("Charlie", "Dog", 2)

dog.display()
dog.celebrate_bd()
