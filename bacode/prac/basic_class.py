class Person:
    
    def __init__(self, name, age):
        """This is the constructor - it runs when we create a new Person"""
        self.name = name  # self.name is an attribute (property) of this person
        self.age = age    # self.age is another attribute
    
    def introduce(self):
        """This is a method (function) that belongs to this class"""
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# Now let's create actual Person objects from our blueprint
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Each person object has its own attributes
print(f"Person 1: {person1.name}, Age: {person1.age}")
print(f"Person 2: {person2.name}, Age: {person2.age}")

# Each person can use the methods
print(person1.introduce())
print(person2.introduce())

# Key concepts:
# - Class: The blueprint (Person)
# - Object/Instance: The actual thing created from the blueprint (person1, person2)
# - Attributes: Properties that store data (name, age)
# - Methods: Functions that belong to the class (introduce)
# - self: Refers to the specific instance of the object