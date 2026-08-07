from collections import Counter
from math import sqrt
from sys import float_info
epsilon = float_info.epsilon # divide by 0 issues? just add epsilon!


class Tracker:
    '''
    This class is responsible for tracking roll and yield stats.
    '''
    def __init__(self):
        '''
        Main constructor. Initializes some constants and fresh calculation.
        '''
        # possible 2d6 rolls and their relative chances
        self.diceCombs = {2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1}
        # denominator of chance fraction
        self.totalCombs = sum(self.diceCombs.values())
        # rolls and yields record
        self.rolls = []
        # dice lock memory per player per dice, aka 'who build on what numbers 
        # and when'. -1 is a sentinel value for 'not built'
        self.diceLocks = {x:{k:-1 for k in self.diceCombs.keys()} for x in (0,1,2,3)}
        self.calculate()


    def calculate(self):
        '''
        Calculates all the statistics.
        '''
        # count all rolls per dice
        self.sampleRolls = Counter(r[0] for r in self.rolls)
        # how much a die should've ideally been rolled out of total rolls
        self.idealRolls = {k:v/self.totalCombs*len(self.rolls) for k,v in self.diceCombs.items()}
        # difference between ideal and actual number of rolls per die
        self.rollDiffs = {k:self.sampleRolls.get(k, 0) - v for k,v in self.idealRolls.items()}
        # "luck" calculation per die. note the magic sqrt, somehow it just 
        # makes it work. this may need more research+rework
        self.luckDiffs = {k:v/(sqrt(len(self.rolls))+epsilon) for k,v in self.rollDiffs.items()}

        # per player per die over all rolls, calculate total yields
        self.playerYields = {x:{k:[roll[1][x] for roll in self.rolls if roll[0] == k].count(True) for k in self.diceCombs.keys()} \
                             for x in (0,1,2,3)}
        # per player per die, calculate how much should've been yielded, 
        # accounting for when the die was locked in.
        #                              | magic boolean math here |
        self.playerIdealYields = {x:{k:(self.diceLocks[x][k]!=-1)*v/self.totalCombs*(len(self.rolls)-self.diceLocks[x][k]) for k,v in self.diceCombs.items()} \
                                  for x in (0,1,2,3)}
        # difference between ideal and actual yields
        self.playerYieldDiffs = {x:{k:self.playerYields[x][k] - v for k,v in self.playerIdealYields[x].items()} \
                                 for x in (0,1,2,3)}
        # "luck" calculation per player per die, accounting for when the die 
        # was locked in. magic sqrt and boolen math are here too.
        self.playerYieldLuck = {x:{k:(self.diceLocks[x][k]!=-1)*v/(sqrt(len(self.rolls)-self.diceLocks[x][k])+epsilon) for k,v in self.playerYieldDiffs[x].items()} \
                                for x in (0,1,2,3)}
        #print(f'{self.playerYieldDiffs=}')
        #print(f'{self.playerYieldLuck=}')

    
    def newRoll(self, roll):
        '''
        Adds new roll to record and recalculates.
        '''
        self.rolls.append(roll)
        self.calculate()


    def deleteLastRoll(self):
        '''
        Removes last roll record if possible and recalculates.
        '''
        try:
            self.rolls.pop()
        except:
            pass
        else:
            self.calculate()

            
    def lockInDice(self, player, dice):
        '''
        Locks in a dice roll as a yielding roll for a player by recording  
        current roll number, aka "build a settlement and remember when".
        '''
        #print(f'locking in {dice} for P{player+1} before roll #{len(self.rolls)+1}')
        self.diceLocks[player][dice] = len(self.rolls)

    def reset(self):
        '''
        Resets the tracker to it's initial state.
        '''
        self.__init__()
    