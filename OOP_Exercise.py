# Parent Base class
# Spurious comment here
class Animal:
    def __init__(self, sound, legs, fur_type):
        self.sound = sound
        self.legs = legs
        self.fur_type= fur_type
        self.type = "unknown"

    def speak(self):
        print(f"The animal of type {self.type} makes the sound of {self.sound}")

    def has_fur(self):
        print(f"The animal of type {self.type} has fur of type {self.fur_type}")

    def number_of_legs(self):
        print(f"The animal of type {self.type} has {self.legs} legs")

class Horse(Animal):

    def __init__(self, sound, legs, fur_type):
        self.sound = sound
        self.legs = legs
        self.fur_type= fur_type
        self.type = "horse"

class Pig(Animal):
    def __init__(self, sound, legs, fur_type):
        self.sound = sound
        self.legs = legs
        self.fur_type= fur_type
        self.type = "pig"

class Roster(Animal):
    def __init__(self, sound, legs, fur_type):
        self.sound = sound
        self.legs = legs
        self.fur_type= fur_type
        self.type = "roster"

if __name__ == "__main__":
    animal1 = Animal("meow", "4", "fluffy")
    animal1.speak()
    animal1.has_fur()
    animal1.number_of_legs()

    # child class Horse from parent class Animal
    print("") # White space for spacing
    horse1 = Horse("neh", "4", "rough")
    horse1.speak()
    horse1.has_fur()
    horse1.number_of_legs()

    # child class Horse from parent class Animal
    Pig1 = Pig("oink", "4", "none")
    print("") # White space for spacing
    Pig1.speak()
    Pig1.has_fur()
    Pig1.number_of_legs()

    # child class Horse from parent class Animal
    Roster1 = Roster("cocka doodle", "2", "feathers")
    print("") # White space for spacing
    Roster1.speak()
    Roster1.has_fur()
    Roster1.number_of_legs()

