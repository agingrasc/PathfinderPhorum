import random


class Dice(object):
    def __init__(self, max_value, min_value=1):
        self.max_value = max_value
        self.min_value = min_value

    def roll(self):
        return random.randint(self.min_value, self.max_value)

    def __eq__(self, other):
        return self.min_value == other.min_value and self.max_value == other.max_value
