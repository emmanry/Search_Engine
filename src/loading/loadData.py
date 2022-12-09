from loading.loadDocs import loadDocs
from loading.loadQueries import loadQueries

def loadData(filenameDoc, filenameQuery):
	# Liste de tous les mots (collection et requêtes)
	words = []
	
	# Chargement des documents et des requêtes
	words, occurencesInDoc, occurencesInCollection = loadDocs(filenameDoc, words)
	words, occurencesInQueries = loadQueries(filenameQuery, words)

	return words, occurencesInDoc, occurencesInCollection, occurencesInQueries
