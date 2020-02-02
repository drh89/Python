import math

print('Hello World')

names = ['Hans', 'Niels', 'Henrik', 'Jørgen', 'Heine', 'William']

res = [namex for namex in names if namex[0] == 'H']
print(str(res))


numbers = list(range(1,101))
for number in numbers: print(pow(number,3))

tuples = []
for name in names: tuples.append(tuple((name,len(name))))
print(tuples)


numString = "1Want2BeNumeric"
numeric = list(numString)
result = [int(num) for num in numeric if num.isdigit() ]
print(result)

dice1 = list(range(1,7))
dice2 = list(range(1,7))
diceSet = set()
for s in dice1:
    for s2 in dice2:
        
            diceSet.add(str(s) + "+" + str(s2))

print(diceSet)

nameDict = {}

for name in names:
    nameDict[name] = len(name)

print(nameDict)

numList = list(range(1,11))
numDict = {}
for num in numList:
    numDict[num] = math.sqrt(num)

print(numDict)


diceDict = {x:0 for x in range(2,13)} # Making dictionary 

for x in dice1: ## Adding throws that can have sum
    for y in dice2:
        diceDict[x+y] += 1
print(diceDict)

for x in diceDict: ## Calculates the probability
     diceDict[x] = str(round(diceDict.get(x)/36*100,2)) + "%"

print(diceDict)