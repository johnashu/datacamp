import urllib.request
import random

#load the data from url
file = urllib.request.urlopen('https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv')
f = file.read()

# convert bitstream into strings
text = f.decode(encoding='utf-8', errors='ignore')

# split single string at the end of lines
lines = text.split('\n')

#  create a dictionary, initialise 

reviews = {}

#fill the dictionary

for line in lines:
    l = line.strip().split("\t")

# training wheels to see more clearly what is in the dictionary

    score = l[0]
    id = l[1]
    title = l[2]
    review = l[3]

    reviews[id] = {'score' : score, 'title' : title, 'review' : review}

# take a random key and display its results
print(reviews[random.choice(list(reviews.keys()))])

# verfiy whether all key are present ..

    # count the number of lines in the file
print("Number of Lines: " + str(len(lines)))

    # count the number of keys in the dictionary
print('Number of Dictionary Keys: ' + str(len(reviews.keys())))


# store all the low scores in a list named lowscores

lowscores = []
for key, value in reviews.items():
    if float(value["score"]) == 1.0: #has to be float
        lowscores.append(key)
    
#print all low sxcore reviews

#for item in lowscores:
 #   print(reviews[item])

# for-loop style to create a subset dictionary of lowscores

forloop = {}
for k in lowscores:
    forloop[k] = reviews[k]

# dictionary comprehension loop

dictcomp = {k : reviews.get(k) for k in lowscores}

# verify they are equal (True)
print(forloop == dictcomp)


from collections import defaultdict

scoredict = defaultdict(list)

for key , value in reviews.items():
    newvalues = {'id' : key, 'title' : value['title'], 'review' : value['review']}
    scoredict[value['score']].append(newvalues)

#print(scoredict.keys())

import re
from collections import defaultdict

freqdict = defaultdict(int)
for item in lowscores:
    review = reviews[item]['review']
    cleantext = re.sub(r'<.*?>', '', review).strip().split() # remove html tag and split by word
    for word in cleantext:
        word.lower()
        freqdict[word] += 1

#print(freqdict)

#order the dictionary and ignore the top 10%.. this is instead of using a "STOP LIST" which contains The, and, is etc

from collections import OrderedDict

#create ordered dictionaty

ordict = OrderedDict(sorted(freqdict.items(), key=lambda item: item[1], reverse=True))

#ignore top 10%

top10 = int(len(ordict.keys())/10)

#print 100 words of the top 90%
print(list(ordict.items())[top10:top10+100])