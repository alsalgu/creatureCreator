#!/usr/bin/python3
# creature.py

import random

eyeDict = {'Red': 'R', 'Rose': 'r', 'Brown': 'B',
           'Blue': 'b', 'Grey': 'G', 'Green': 'g'}
furDict = {'Black': 'B', 'Brown': 'b', 'White': 'W', 'Wheat': 'w'}
sex = ['Male', 'Female']

allCreatures = []
babyCreatures = []


class Creature:
    def __init__(self, name, sex):
        # Generate profile of genetic information
        self.name = name
        self.sex = sex
        # Create genes from two randomly selected values from the dictionary
        self.furGene = random.choice(
            list(furDict.values())) + random.choice(list(furDict.values()))
        self.eyeGene = random.choice(
            list(eyeDict.values())) + random.choice(list(eyeDict.values()))
        # Default colors in case I miss a genotype combination in the results
        self.furColor = 'Brown'
        self.eyeColor = 'Green'
        # Placeholders for parentage
        self.mom = 'Unknown'
        self.dad = 'Unknown'
        # Color RNG based on respective gene
        getFurColor(self, self.furGene)
        getEyeColor(self, self.eyeGene)
        # Add creature to list for easy access later.
        allCreatures.append(self.name)


class Baby:
    def __init__(self, mom, dad):
        if mom.sex == 'Female' and dad.sex == 'Male':
            self.sex = random.choice(sex)
            self.name = input("Congrats, it's a " + self.sex + "! What would you like to name the baby? ")
            self.mom = mom.name
            self.dad = dad.name
            # Generate fur gene but from mom and dad's genes by selecting
            # one char from each
            self.furGene = random.choice(
                mom.furGene) + random.choice(dad.furGene)
            self.furColor = "Brown"
            self.eyeGene = random.choice(
                mom.eyeGene) + random.choice(dad.eyeGene)
            self.eyeColor = "Green"
            getEyeColor(self, self.eyeGene)
            getFurColor(self, self.furGene)
            babyCreatures.append(self.name)
        else:
            print('Parents are incompatible')
            return


def listPedigree(name):
    # Prints creature variables in a nice paragraph
    print(name.name + " has " + name.furColor + " fur.\n" +
          name.name + " has " + name.eyeColor + " eyes.\n" +
          name.name + " is a " + name.sex + ".\n" +
          "Parents: " + name.mom + ", " + name.dad)


def getEyeColor(creature, gene):
    # R - red, B - Brown, G - Grey
    # r - rose, b - blue, g - green

    # Check to see if there's any dominant alelles (capitals) in gene string
    if any(map(str.isupper, gene)):
        outcome = []
        # If there is, add color name to list of outcomes
        if ('R' in gene):
            outcome.append('Red')
        if ('G' in gene):
            outcome.append('Grey')
        if ('B' in gene):
            outcome.append('Brown')
        # Choose a color from the list of outcomes and assign as eyeColor
        creature.eyeColor = random.choice(outcome)
    # If no caps, go through lowercases
    else:
        outcome = []
        # Add color to outcome list if corresponding letter is present
        if ('r' in gene):
            outcome.append('Rose')
        if ('g' in gene):
            outcome.append('Green')
        if ('b' in gene):
            outcome.append('Blue')
        if ('r' in gene) and ('b' in gene):
            outcome = []
            outcome.append('Purple')
        if ('b' in gene) and ('g') in gene:
            outcome = []
            outcome.append('Teal')
        # Set eyeColor to random selection from the possible outcomes
        creature.eyeColor = random.choice(outcome)


def getFurColor(creature, gene):
    # B - Black, W - White
    # b - Brown, w - Wheat
    # Works exactly the same as getEyeColor but with furDict
    if any(map(str.isupper, gene)):
        outcome = []
        if ('B' in gene):
            outcome.append('Black')
        if ('W' in gene):
            outcome.append('White')
        if ('W' in gene) and ('B' in gene):
            outcome = []
            outcome.append('Grey')
        creature.furColor = random.choice(outcome)
    else:
        outcome = []
        if ('b' in gene):
            outcome.append('Brown')
        if ('w' in gene):
            outcome.append('Wheat')
        if ('b' in gene) and ('w' in gene):
            outcome = []
            outcome.append('Caramel')
        creature.furColor = random.choice(outcome)
