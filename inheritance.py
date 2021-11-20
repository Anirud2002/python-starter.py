class Mammal:
    def walk(self):
        print('Walk')


class Dog(Mammal):
    def bark(self):
        print('Bark')


class Cat(Mammal):
    def meow(self):
        print('Meow')


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.meow()