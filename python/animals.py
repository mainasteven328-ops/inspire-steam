#name : steve lawrence
#date : 23.02.2026
# program : to show inheritance in python


class Animal():
    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"the animal weighs {weight}")

    def eat (self,food):
        print(f"the animal eats {food}")



class Dog(Animal):
    def __init__(self,species,height,breed):
        supper().__init__(species,weight,food)
        self.breed = breed
        self.colour = colour
        self.height = height
def barks(self,barks):
        print("the dog says woof woof {bark}")

class horse(Animal):
    def __init__(self,species,weight,food):
        

    def neigh(self,neigh):
        print(f"the animal neighs {neigh}")

    def eat (self,food):
        print(f"the animal eats {food}")