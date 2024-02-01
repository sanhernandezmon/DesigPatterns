# Abstract Product A
class Animal:
    def speak(self):
        pass

# Concrete Product A1
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Concrete Product A2
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Abstract Product B
class Color:
    def fill(self):
        pass

# Concrete Product B1
class BrownColor(Color):
    def fill(self):
        return "Brown color filled"

# Concrete Product B2
class WhiteColor(Color):
    def fill(self):
        return "White color filled"

# Abstract Factory
class AbstractFactory:
    def create_animal(self):
        pass
    
    def create_color(self):
        pass

# Concrete Factory 1
class PetFactory(AbstractFactory):
    def create_animal(self):
        return Dog()

    def create_color(self):
        return BrownColor()

# Concrete Factory 2
class WildAnimalFactory(AbstractFactory):
    def create_animal(self):
        return Cat()

    def create_color(self):
        return WhiteColor()

# Client Code
def create_and_speak(factory):
    animal = factory.create_animal()
    color = factory.create_color()

    print(f"{type(animal).__name__} says: {animal.speak()}")
    print(f"Color: {color.fill()}")

# Usage
pet_factory = PetFactory()
wild_animal_factory = WildAnimalFactory()

print("Pet Factory:")
create_and_speak(pet_factory)

print("\nWild Animal Factory:")
create_and_speak(wild_animal_factory)
