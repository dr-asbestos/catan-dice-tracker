from random import randint, choices
from collections import Counter
from sys import float_info
epsilon = float_info.epsilon


class Tracker:
    '''
    todo write me
    '''
    def __init__(self):
        '''
        todo write me
        '''
        self.diceCombs = {2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1}
        self.totalCombs = sum(self.diceCombs.values())
        self.rolls = []
        self.sampleRolls = Counter()
        self.idealRolls = {}
        self.rollDiffs = {}
        self.luckDiffs = {}
        self.calculate()

    def calculate(self):
        '''
        todo write me
        '''
        self.sampleRolls = Counter(self.rolls)
        self.idealRolls = {k:v/self.totalCombs*len(self.rolls) for k,v in self.diceCombs.items()}
        self.rollDiffs = {k:self.sampleRolls.get(k, 0) - v for k,v in self.idealRolls.items()}
        self.luckDiffs = {k:v/(len(self.rolls)+epsilon) for k,v in self.rollDiffs.items()}

    
    def newRoll(self, roll):
        '''
        todo write me
        '''
        try:
            if not (2 <= int(roll) <= 12):
                raise
        except:
            print(f'Invalid dice: {roll}')
        else:
            self.rolls.append(int(roll))
            self.calculate()

    def deleteLastRoll(self):
        '''
        todo write me
        '''
        try:
            self.rolls.pop()
        except:
            pass
        self.calculate()
            
