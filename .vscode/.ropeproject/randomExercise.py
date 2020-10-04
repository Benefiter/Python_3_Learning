import random


class Dice:

    def roll_die(self):
        return random.randint(1,6)


    def roll(self):
        return self.roll_die(), self.roll_die()

dice = Dice()

print (dice.roll())