import random
from requests import request


words = []

numberofphrases = int(input("How many phrases would you like to generate? "))

with open('BIP39 words.txt') as wordlist:
  for word in wordlist:
    words.append(word.strip())
    

for x in range(numberofphrases):
  seed = []
  for i in range(12):
    seed.append(random.choice(words))

  res = request('GET', 'http://localhost:3000/api/' + ' '.join(seed))

  if(res.json()['isValid'] == True):
    with open('valid phrases.txt', 'a') as f:
      f.write('\n'+' '.join(seed))

  print(' '.join(seed)+ ' : ' + str(res.json()['isValid']))