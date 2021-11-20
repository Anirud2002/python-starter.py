import random


class Dice:
    def roll(self):
        return random.randint(1,6), random.randint(1,6)


player1 = Dice()
print(player1.roll())

