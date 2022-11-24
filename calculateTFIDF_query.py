import numpy as np

def calculateTFIDF_query(wordsIDF, occurencesInQueries):
	query_TFIDF = {}

	for query in occurencesInQueries:
		sizeQuery = sum(occurencesInQueries[query])
		wordsTF = (np.array(occurencesInQueries[query]) / sizeQuery)
		query_TFIDF[query] = wordsTF[:len(wordsIDF)] * wordsIDF

	return query_TFIDF
