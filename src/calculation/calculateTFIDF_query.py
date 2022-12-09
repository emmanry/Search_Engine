import numpy as np

def calculateTFIDF_query(wordsIDF, occurencesInQueries):
	'''
	Calcule le TFIDF de chaque mot pour chaque requête
	
	@inputs
		- wordsIDF : IDF de chaque mot de la collection ;
		- occurencesInQueries : Dictionnaire qui a pour clé l'id de chaque requête et pour valeur le vecteur du nombre d'occurence de chacun des mots de la requête.

	@output
		- query_TFIDF : Dictionnaire qui a pour clé l'id de chaque requête et pour valeur le vecteur du TFIDF de chacun des mots de la requête.
	'''
	query_TFIDF = {}

	for query in occurencesInQueries:
		sizeQuery = sum(occurencesInQueries[query])
		wordsTF = (np.array(occurencesInQueries[query]) / sizeQuery)
		query_TFIDF[query] = wordsTF[:len(wordsIDF)] * wordsIDF

	return query_TFIDF
