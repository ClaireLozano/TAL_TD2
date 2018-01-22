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
		dictionnary = {}
		for key, value in data.iteritems():

			# Return nb similar words
			nbcount = compareWords(listSortedWords, value)
			# Purcentage calcul
			res = nbcount/float(n)
			dictionnary[key] = res

		l = sorted([[y, x] for x,y in dictionnary.items()], reverse=True)

		if l[0][0] > 0.60:
			# Print
			print "\n"
			print "Le langage utilise dans ce fichier est : " + str(l[0][1])
			print "Avec un pourcentage de " + str(l[0][0])
			print "\n"
			return str(l[0][1])
		else:
			return None


def compareWords(listSortedWords, jsonFile):
	count = 0
	for w in listSortedWords:
		for v in jsonFile:
			if w[1] == v[1]:
				count += 1
	return float(count)


def evaluation(files, n, jsonFile):
	# Init
	TP = 0
	FP = 0
	FN = 0

	for f in files:
		# get words
		words = getDataFromTextFile(f)
		# Sort word - keep les 8 mot les plus utilises
		listSortedWords = sortByWord(words, int(n))

		# Find the language of the file
		languageFounded = findLanguage(listSortedWords, jsonFile, int(n))

		# Verite terrain
		tab = f.split("/")
		l = tab[1]
		
		# Comparaison de verite terrain avec le resultat retourne 
		if languageFounded == l:
			TP += 1
		elif languageFounded is None: # Ne return rien 
			FP += 1
		elif languageFounded != l: # Return une langue fausse
			FN += 1

	
	# Calcul
	Rappel = float(TP)/(TP+FN)
	Presicion = float(TP)/(TP+FP)
	FMesure = (2*Rappel*Presicion)/(Presicion+Rappel)

	# Print
	print "TP : " + str(TP)
	print "FN : " + str(FN)
	print "FP : " + str(FP)
	print "Rappel : " + str(Rappel)
	print "Presicion : " + str(Presicion)
	print "FMesure : " + str(FMesure)
	print "\n"


# python TAL2TestAllFiles.py 8 frequence.json corpus_multi2/*/test/*.html
# Get input
n = sys.argv[1]
jsonFile = sys.argv[2]
files = sys.argv[3:]


evaluation(files, n, jsonFile)

