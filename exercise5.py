class Person:
    # this is a constructor function
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Talk to me {self.name}')


person1 = Person('Anirud')
person1.talk()