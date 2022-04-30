import random

from requests import request


fours =[]
fives =[]
sixes =[]
sevens =[]

with open('words.txt') as wordlist:
    for line in wordlist:
        if len(line.strip()) == 4:
          fours.append(line.strip())
        elif len(line.strip()) == 5:
          fives.append(line.strip())
        elif len(line.strip()) == 6:
          sixes.append(line.strip())
        elif len(line.strip()) == 7:
          sevens.append(line.strip())

print(len(fours), len(fives), len(sixes), len(sevens))  


numberofphrases = int(input("How many phrases would you like to generate? "))

for x in range(numberofphrases):
  seed = []
  for x in range(12):
    #get a random word from fours, fives, sixes or sevens
    randomone = random.choice(fours)
    randomtwo = random.choice(fives)
    randomthree = random.choice(sixes)
    randomfour = random.choice(sevens)
    randomselect = random.randint(0, 3)
    if (randomselect == 0):
      seed.append(randomone)
    elif (randomselect == 1):
      seed.append(randomtwo)
    elif (randomselect == 2):
      seed.append(randomthree)
    elif (randomselect == 3):
      seed.append(randomfour)

  res = request('GET', 'http://localhost:3000/api/' + ' '.join(seed))

  if(res.json()['isValid'] == True):
    with open('valid phrases.txt', 'a') as f:
      f.write('\n'+' '.join(seed))

  print(' '.join(seed)+ ' : ' + str(res.json()['isValid']))

