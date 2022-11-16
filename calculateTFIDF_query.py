from scipy.spatial import distance
import numpy as np

def calculateTFIDF_query(wordInCollection, wordInQuery):	
	for query in wordInQuery:
		sizeQuery = 0
		for word in wordInQuery[query]:
			print(wordInQuery)
			sizeQuery += wordInQuery[query][word][0]
		for word in wordInQuery[query]:
			TF = wordInQuery[query][word][0] / sizeQuery
			wordInQuery[query][word][1] = TF * wordInCollection[word][1]
	
	return wordInQuery
