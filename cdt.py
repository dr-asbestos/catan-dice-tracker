from random import randint, choices
from collections import Counter
from pprint import pprint

# rolling paramenters
nRolls = 360
diceCombs = {2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1}
# derived ideal stats
totalCombs = sum(diceCombs.values())
idealRolls = {k:v/totalCombs*nRolls for k,v in diceCombs.items()}
print(idealRolls)

# generate random dice rolls
sampleRolls = Counter(choices(list(diceCombs.keys()), diceCombs.values(), k=nRolls))
print(sampleRolls)
# number of rolls differences between ideal and actual rolls
rollDiffs = {k:sampleRolls.get(k, 0) - v for k,v in idealRolls.items()}
pprint(rollDiffs)
# same but ratio form
luckDiffs = {k:v/nRolls for k,v in rollDiffs.items()}
pprint(luckDiffs)
# pretty print
formatted = {k:f'{v:+.2%}' for k,v in luckDiffs.items()}
pprint(formatted)