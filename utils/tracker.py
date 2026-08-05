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
        self.calculate()


    def calculate(self):
        '''
        todo write me
        '''
        self.sampleRolls = Counter(r[0] for r in self.rolls)
        self.idealRolls = {k:v/self.totalCombs*len(self.rolls) for k,v in self.diceCombs.items()}
        self.rollDiffs = {k:self.sampleRolls.get(k, 0) - v for k,v in self.idealRolls.items()}
        self.luckDiffs = {k:v/(len(self.rolls)+epsilon) for k,v in self.rollDiffs.items()}

        self.playerYields = {x:{k:[roll[1][x] for roll in self.rolls if roll[0] == k].count(True) for k in self.diceCombs.keys()} for x in (0,1,2,3)}

        #print(f'{self.playerYields=}')

    
    def newRoll(self, roll):
        '''
        todo write me
        '''
        self.rolls.append(roll)
        self.calculate()

    def deleteLastRoll(self):
        '''
        todo write me
        '''
        try:
            self.rolls.pop()
        except:
            pass
        else:
            self.calculate()
            
