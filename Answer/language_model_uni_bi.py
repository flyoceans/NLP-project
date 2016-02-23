########################################
# This script is a helpful tool for locating the position of context corresponding to the quesition.
# Calculating N-gram language model probabilites of context sentence.


import math
import sys
import operator

########################################
# Language model functions

def unigram(fileName):
	f = open(fileName, 'r')
	uniDic = {}
	count = 0
	for line in f.readlines():
		line = line.lower().split()
		#line.append("</s>")
		for word in line:
			count += 1
			if uniDic.has_key(word):
				uniDic[word] += 1
			else :
				uniDic[word] = 1
	f1 = open('output.txt','w')
	sort = sorted(uniDic.items(), key=operator.itemgetter(1), reverse=True)
	for key in sort:
		#if key[1] < 5:
		#f1.write(key[0] + ':' + str(math.log(float(key[1])/count)) + '\n')
		f1.write(key[0] + ':' + str(float(key[1])/count) + '\n')
	f1.write(str(count) + '\n')
	f.close()
	f1.close()	
	return count,uniDic

def bigram(fileName):
	f = open(fileName, 'r')
	biDic = {}
	uniDic = {}
	count = 0
	for line in f.readlines():
		line = line.lower().split()
		#line.append("</s>")
		line.insert(0, "<s>")
		for i in range(1, len(line)-1):
			biword = line[i-1] + ' ' + line[i]
			if not biDic.has_key(biword):
				count += 1
				biDic[biword] = 1
				if not uniDic.has_key(line[i-1]):
					uniDic[line[i-1]] = 1
					#uniDic[""] = 1
				else:
					uniDic[line[i-1]] += 1		
					#uniDic[""] += 1	
			else :
				biDic[biword] += 1
				uniDic[line[i-1]] += 1		
				#uniDic[""] += 1		
	f1 = open('output','a')
	sort = sorted(biDic.items(), key=operator.itemgetter(1), reverse=True)
	s = {}
	for key in sort:
		word = key[0].split()
		word.pop()
		myword = " ".join(word)
		s[key[0]] = float(key[1])/uniDic[myword]
		#f1.write(key[0] + ':' + str(math.log(float(key[1])/uniDic[myword])) + '\n')
		#f1.write(key[0] + ':' + str(float(key[1])/uniDic[myword]) + '\n')
	sort = sorted(s.items(), key=operator.itemgetter(1), reverse=True)	
	for key in sort:
		f1.write(key[0] + ':' + str(key[1]) + '\n')
	f1.write(str(count) + '\n')
	f.close()
	f1.close()	
	return biDic

def trigram(fileName):
	f = open(fileName, 'r')
	biDic = {}
	triDic = {}
	count = 0
	for line in f.readlines():
		line = line.lower().split()
		#line.append("</s>")
		line.insert(0, "<s>")
		for i in range(2, len(line)-1):
			biword = line[i-2] + ' ' + line[i-1]
			triword = line[i-2] + ' ' + line[i-1] + ' ' + line[i]
			if not triDic.has_key(triword):
				count += 1
				triDic[triword] = 1
				if not biDic.has_key(biword):
					biDic[biword] = 1
					#biDic[""] = 1
				else:
					biDic[biword] += 1
			else :
				triDic[triword] += 1
				biDic[biword] += 1
				#biDic[""] += 1	
	f1 = open('output','a')
	sort = sorted(triDic.items(), key=operator.itemgetter(1), reverse=True)
	s = {}
	for key in sort:
		word = key[0].split()
		word.pop()
		myword = " ".join(word)
		s[key[0]] = float(key[1])/biDic[myword]
		#f1.write(key[0] + ':' + str(math.log(float(key[1])/biDic[myword])) + '\n')
		#f1.write(key[0] + ':' + str(float(key[1])/biDic[myword]) + '\n')
	sort = sorted(s.items(), key=operator.itemgetter(1), reverse=True)
	for key in sort:
		f1.write(key[0] + ':' + str(key[1]) + '\n')
	f1.write(str(count) + '\n')
	f.close()
	f1.close()	
	return triDic

#unigram(fileName)
#bigram(fileName)
#trigram(fileName)

