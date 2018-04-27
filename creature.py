#!/usr/bin/python3
# creature.py

# Template that will create instances of creatures.


class Creature:
    # Variables shared by all instances
    kind = 'creature'
    # Variables unique to each instance.

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
