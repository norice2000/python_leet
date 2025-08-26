class Person:
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi {self.name}, you must be {self.age}!"
    

#instantiate class with object
person1 = Person('champ', '12')
person2 = Person('lulu', '10')

print(person1.name, person1.age)

# using method inside class
print(person1.introduce())