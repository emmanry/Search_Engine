from loading.loadDocs import loadDocs
from loading.loadQueries import loadQueries

def loadData(filenameDoc, filenameQuery):
	'''
	Charge en mémoire les données à traiter
	
	@inputs
		- filenameDoc : chemin du document de la collection de documents ;
		- filenameQuery : chemin du document de la collection de requêtes.
	
	@output
		- words : Liste de tous les mots (collection + requêtes) ;
		- occurencesInDoc : Dictionnaire qui a pour clé l'id de chaque document et pour valeur le vecteur du nombre d'occurence de chacun des mots du document ;
		- occurencesInCollection : Liste du nombre de documents dont le mot à l'indice i apparaît au moins une fois ;
		- occurencesInQueries : Dictionnaire qui a pour clé l'id de chaque requête et pour valeur le vecteur du nombre d'occurence de chacun des mots de la requête.
	'''
	# Liste de tous les mots (collection et requêtes)
	words = []
	
	# Chargement des documents et des requêtes
	words, occurencesInDoc, occurencesInCollection = loadDocs(filenameDoc, words)
	words, occurencesInQueries = loadQueries(filenameQuery, words)

	return words, occurencesInDoc, occurencesInCollection, occurencesInQueries
