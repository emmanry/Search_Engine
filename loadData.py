import loadDocs
import loadQueries

def loadData(filenameDoc, filenameQuery):
	words = []
	
	words, occurencesInDoc, occurencesInCollection = loadDocs.loadDocs(filenameDoc, words)
	words, occurencesInQueries = loadQueries.loadQueries(filenameQuery, words)

	return words, occurencesInDoc, occurencesInCollection, occurencesInQueries
