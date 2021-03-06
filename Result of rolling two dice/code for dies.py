from random import randint

class Die:
    """a class representing a single die"""

    def __init__(self, num_sides=6):
        "A six sided die"
        self.num_sides = num_sides
    
    def roll(self):
        """return a random value"""
        return randint(1, self.num_sides)