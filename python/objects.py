# name : steve lawrence
# date: 19/2/2026
# program : to create objects
class Human:
    # first we define the attributes of a human being
    type = "mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "nairobi"

    # we create a constructor of object
    # the constructor will be used to create the copies of the object
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age
    def tell_story(self):
        print(f" hello , i am {self.human_name} , this is my story")
        print("rest in peace to my grandma she got hit a bazooka")

        # creating the objects
puhbender =  Human("puhbender", 17)
kingofthejungletypeshit= Human("kingofthejungletypeshit", 19)

# let the humans created  to do things
puhbender.tell_story()
print("puhbender age is :", puhbender.human_age)
# modify one of the objects without modifying all the objects

puhbender.city = "fineshyts puh"
print("puhbenders location:", puhbender.city)
print("kingofthejungletypeshits loction:", kingofthejungletypeshit.city)