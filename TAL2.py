import os
import sys
import matplotlib.pyplot as plt
import json

def getDataFromTextFile(folder):
	dictionnary = {}
	for f in folder:
		pathSplit = f.split('/')
		language = pathSplit[1]
		data = []
		with open(f) as inp:
			for line in inp:
				words = splitByWord(line)
				for w in words:
					data.append(w)
		if dictionnary.get(language) is not None:
			resToAppend = dictionnary[language]
			dictionnary[language] = dictionnary[language] + data
		else :
			dictionnary[language] = data
	return dictionnary


def splitByWord(line):
	wordsList = []
	words = line.split()
	for word in words:
		wordsList.append(word)
	return wordsList


def sortByWord(words):
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
	return l[0:8]

# python TAL2.py corpus_multi2/*/appr/*.html
# Get input
folderAppr = sys.argv[1:]
# get words
words = getDataFromTextFile(folderAppr)

# Write in a json file
file = open('frequence.json', 'w+')
file.write("{")

for language, element in words.items():
	listSortedWords = sortByWord(element)
	file.write('\n\t"' + language + '"' + " : ") 
	json.dump(listSortedWords, file)
	file.write(",") 

file.seek(-1, os.SEEK_END)
file.truncate()
file.write("\n}" + "\n")
file.close()
