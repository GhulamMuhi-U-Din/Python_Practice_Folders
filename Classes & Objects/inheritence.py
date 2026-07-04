# inheritence in classes

class Animal:

    def eat(self):
        print("Eating...")

class Dog(Animal):
    pass

class Cat(Animal):
    pass
spike = Dog()
spike.eat()

tom = Cat()
tom.eat()

# method overriding

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()

# super (whe nwe want to call parent's method)

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Bark")


dog = Dog()

dog.sound()