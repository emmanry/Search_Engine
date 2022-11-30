import loadDocs
import loadQueries

def loadData(filenameDoc, filenameQuery):
	# Liste de tous les mots (collection et requêtes)
	words = []
	
	# Chargement des documents et des requêtes
	words, occurencesInDoc, occurencesInCollection = loadDocs.loadDocs(filenameDoc, words)
	words, occurencesInQueries = loadQueries.loadQueries(filenameQuery, words)

	return words, occurencesInDoc, occurencesInCollection, occurencesInQueries
