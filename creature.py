#!/usr/bin/python3
# creature.py

import random

eyeDict = {'Red': 'R', 'Rose': 'r', 'Brown': 'B',
           'Blue': 'b', 'Grey': 'G', 'Green': 'g'}
furDict = {'Black': 'B', 'Brown': 'b', 'White': 'W', 'Wheat': 'w'}
maneDict = {'Black': 'B', 'Brown': 'b', 'White': 'W', 'Wheat': 'w'}
hornToggle = {'Yes': 'Y', 'No': 'y'}
hornType = {'Curved': 'C', 'Straight': 'c'}
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
        self.maneGene = random.choice(
            list(maneDict.values())) + random.choice(list(maneDict.values()))
        self.hornGene = random.choice(
            list(hornType.values())) + random.choice(list(hornType.values()))
        self.hornToggled = random.choice(
            list(hornToggle.values())) + random.choice(list(hornToggle.values()))
        # Default colors in case I miss a genotype combination in the results
        self.furColor = 'Brown'
        self.eyeColor = 'Green'
        self.maneColor = 'White'
        self.hornShow = 'Yes'
        self.hornShape = 'Straight'
        # Placeholders for parentage
        self.parent1 = 'Unknown'
        self.parent2 = 'Unknown'
        # Color RNG based on respective gene
        getFurColor(self, self.furGene)
        getEyeColor(self, self.eyeGene)
        getManeColor(self, self.maneColor)
        getHornShow(self, self.hornToggled)
        getHornType(self, self.hornGene)
        # Add creature to list for easy access later.
        allCreatures.append(self.name)


class Baby:
    def __init__(self, parent1, parent2):
        self.sex = random.choice(sex)
        self.name = input("Congrats, it's a " + self.sex +
                          "! What would you like to name the baby? ")
        self.parent1 = parent1.name
        self.parent2 = parent2.name
        # Generate gene genotype with parents' values
        self.furGene = random.choice(
            parent1.furGene) + random.choice(parent2.furGene)
        self.eyeGene = random.choice(
            parent1.eyeGene) + random.choice(parent2.eyeGene)
        self.maneGene = random.choice(
            parent1.maneGene) + random.choice(parent2.maneGene)
        self.hornGene = random.choice(
            parent1.hornGene) + random.choice(parent2.hornGene)
        self.hornToggled = random.choice(
            parent1.hornGene) + random.choice(parent2.hornGene)
        # Default colors in case getFunctions fail
        self.furColor = "Brown"
        self.eyeColor = "Green"
        self.maneColor = "White"
        self.hornShow = "Yes"
        self.hornShape = "Curved"
        # Functions to retrieve genes' phenotypes
        getEyeColor(self, self.eyeGene)
        getFurColor(self, self.furGene)
        getManeColor(self, self.maneGene)
        getHornShow(self, self.hornToggled)
        getHornType(self, self.hornGene)
        # Add to a list of babies
        babyCreatures.append(self.name)


def getPedigree(name):
    # Prints creature variables in a nice paragraph
    print(name.name + " has " + name.furColor + " fur.\n" +
          name.name + " has " + name.eyeColor + " eyes.\n" +
          name.name + " has a " + name.maneColor + " mane.\n" +
          name.name + " is a " + name.sex)
    if name.hornShow == "Show":
        print(name.name + " has horns and they are " + name.hornShape + ".")
    else:
        print(name.name + " has no horns.")
    print("Parents: " + name.parent1 + ", " + name.parent2)


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


def getManeColor(creature, gene):
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
        creature.maneColor = random.choice(outcome)
    else:
        outcome = []
        if ('b' in gene):
            outcome.append('Brown')
        if ('w' in gene):
            outcome.append('Wheat')
        if ('b' in gene) and ('w' in gene):
            outcome = []
            outcome.append('Caramel')
        creature.maneColor = random.choice(outcome)


def getHornShow(creature, gene):
    # Y - yes, y - n.
    if any(map(str.isupper, gene)):
        creature.hornShow = 'Show'
    else:
        creature.hornShow = 'NoShow'


def getHornType(creature, gene):
    # hornType = {'Curved': 'C', 'Straight': 'c'}
    if gene == 'CC' or 'Cc':
        creature.hornShape = 'Curved'
    if gene == 'cC':
        creature.hornShape = 'Spiral'
    if gene == 'cc':
        creature.hornShape = 'Straight'
