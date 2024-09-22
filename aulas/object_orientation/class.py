class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')
        

pi = Person('John', 30)
pi.say_hello()

pi2 = Person('Jane', 25)
pi2.say_hello()
