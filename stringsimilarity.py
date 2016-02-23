import nltk
from nltk import *

personalqs = ["who","whom"]
locqs = ["where"]

def narrow(question,possibles):
	result = []
	pers = False
	loc = False
	for word in question:
		word = word.lower()
		if word in personalqs:
			pers = True
			break
		elif word in locqs:
			loc = True
			break
	for poss in possibles:
		poss = nltk.pos_tag(poss)
		tree = nltk.ne_chunk(poss)
		for child in tree:
			if pers == True:
				if len(child) == 1 and (child.label() == "PERSON" or child.label() == "GPE"):
					result.append(poss)
					break
			elif loc == True:
				if len(child) == 1 and child.label() == "GPE":
					result.append(poss)
					break
	return result

def findBest(sentence,possibles):
	v1 = dict()
	maxSim = 0
	best = ""
	for word in sentence:
		if word in v1:
			v1[word] += 1
		else:
			v1[word] = 1
	for poss in possibles:
		v2 = dict()
		for word in poss:
			if word in v2:
				v2[word] += 1
			else:
				v2[word] = 1
		sim = dotSim(v1,v2)
		if sim > maxSim:
			best = poss
			maxSim = sim
	return best


def dotSim(v1,v2):
	result = 0
	for word in v1:
		if word in v2:
			result+= v1[word]*v2[word]
	return result

sentence = "Where was John born?"
sentence = nltk.word_tokenize(sentence)
possibles = ["John lives in Pittsburgh", "John was born in Boston", "John likes pizza"]
for i in xrange(len(possibles)):
	possibles[i] = nltk.word_tokenize(possibles[i])
possibles = narrow(sentence,possibles)
sentence = nltk.pos_tag(sentence)

print findBest(sentence,possibles)


sentence = "Who ate the pizza?"
sentence = nltk.word_tokenize(sentence)
possibles = ["John ate at the movie", "Mary ate the pizza", "Bob bought the pizza"]
for i in xrange(len(possibles)):
	possibles[i] = nltk.word_tokenize(possibles[i])
possibles = narrow(sentence,possibles)
sentence = nltk.pos_tag(sentence)

print findBest(sentence,possibles)
