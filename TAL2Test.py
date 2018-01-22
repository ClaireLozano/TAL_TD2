import os
import sys
import matplotlib.pyplot as plt
import json

def getDataFromTextFile(file):
	data = []
	with open(file) as inp:
		for line in inp:
			words = splitByWord(line)
			for w in words:
				data.append(w)
	return data


def splitByWord(line):
	wordsList = []
	words = line.split()
	for word in words:
		wordsList.append(word)
	return wordsList


def sortByWord(words, n):
	dictionnary = {}
	for w in words:
		if len(dictionnary):
			if w in dictionnary.keys():
				dictionnary[w] = dictionnary.get(w) + 1
			else:
				dictionnary[w] = 1
		else : 
			dictionnary[w] = 1
	l = sorted([[y, x] for x,y in dictionnary.items()], reverse=True)
	return l[0:n]


def findLanguage(listSortedWords, jsonFile, n):
	with open(jsonFile, 'r') as f:
		data = json.load(f)
		f.close()
		for key, value in data.iteritems():

			# Return nb similar words
			nbcount = compareWords(listSortedWords, value)
			# Purcentage calcul
			res = nbcount/float(n)

			if res > 0.75:
				# Print
				print "\n"
				print "Le langage utilise dans ce fichier est : " + str(key)
				print "Avec un pourcentage de " + str(res*100) + "%"
				# print "Rappel : " + str(Rappel) 
				# print "Presicion : " + str(Presicion) 
				# print "F-mesure : " + str(FMesure) 
				print "\n"


def compareWords(listSortedWords, jsonFile):
	count = 0
	for w in listSortedWords:
		for v in jsonFile:
			if w[1] == v[1]:
				count += 1
	return float(count)



# python TAL2test.py corpus_multi2/es/test/2009-01-09_celex_IP-09-26.es.html frequence.json 8
# Get input
file = sys.argv[1]
jsonFile = sys.argv[2]
n = sys.argv[3]

# get words
words = getDataFromTextFile(file)
# Sort word - keep les 8 mot les plus utilises
listSortedWords = sortByWord(words, int(n))

# Find the language of the file
findLanguage(listSortedWords, jsonFile, int(n))

