#!/usr/bin/python3
# creature.py

import random

furDict = {'Black': 'B', 'Brown': 'b', 'White': 'W', 'Wheat': 'w'}
furResults = {'Black': ['BB', 'Bb', 'Bw', 'bB', 'wB'], 'Caramel': ['wb', 'bw'], 'Brown': [
    'bb'], 'White': ['Ww', 'wW', 'Wb', 'bW', 'WW'], 'Grey': ['WB', 'BW'], 'Wheat': 'ww'}
sex = ['Male', 'Female']

allCreatures = []
babyCreatures = []


class Creature:
    def __init__(self, name, sex):
        # Generate profile of genetic information
        self.name = name
        self.sex = sex
        # Create fur gene from two randomly selected values from the dictionary
        self.furGene = random.choice(
            list(furDict.values())) + random.choice(list(furDict.values()))
        # Default fur color in case I miss a genotype combination in the results
        self.furColor = 'Blue'
        # Placeholders for parentage
        self.mom = 'Unknown'
        self.dad = 'Unknown'
        # Go through the keys in furResults and see if any match the fur gene
        for key in furResults.keys():
            if self.furGene in furResults[key]:
                # If generated furGene has a match, replace furColor name
                # with respective key from the furResults
                self.furColor = str(key)
        # Add creature to list for easy access later.
        allCreatures.append(self.name)


class Baby:
    def __init__(self, mom, dad):
        if mom.sex == 'Female' and dad.sex == 'Male':
            self.name = input("What would you like to name the baby? ")
            self.sex = random.choice(sex)
            self.mom = mom.name
            self.dad = dad.name
            # Generate fur gene but from mom and dad's genes by selecting
            # one char from each
            self.furGene = random.choice(
                mom.furGene) + random.choice(dad.furGene)
            self.furColor = 'Blue'
            for key in furResults.keys():
                if self.furGene in furResults[key]:
                    self.furColor = str(key)
            babyCreatures.append(self.name)
        else:
            print('Parents are incompatible.')


def listPedigree(name):
    print(name.name + " has " + name.furColor + " fur.\n" +
          name.name + " is a " + name.sex + ".\n" +
          "Parents: " + name.mom + ", " + name.dad "\n")
