# Projet d'analyse du langage

Ce projet a été réalisé dans le cadre universitaire par deux étudiantes de master ICONE à l'université de La Rochelle.

## Objectifs

L'objectif est de reconnaitre la langue d'un fichier en utilisant les mots les plus commun d'une langue. On déterminera aussi son pourcentage de précision, le rappel et la FMesure des résultats.


TAL2.py : Création du fichier json
	ligne de commande : `python TAL2.py corpus_multi2/*/appr/*.html`
	
TAL2Test.py : Analyse d'un seul fichier et reconnaissance de la langue
	ligne de commande : `python TAL2test.py corpus_multi2/es/test/2009-01-09_celex_IP-09-26.es.html frequence.json 8`

TAL2TestAllFiles.py : Analyse de plusieurs fichiers
	ligne de commande : `python TAL2TestAllFiles.py 8 frequence.json corpus_multi2/*/test/*.html`