from scipy.spatial import distance
import numpy as np

def calculateTFIDF(wordInDoc, wordInCollection):
	nbDocs = len(wordInDoc)
	
	for doc in wordInDoc:
		sizeDoc = 0
		for word in wordInDoc[doc]:
			sizeDoc += wordInDoc[doc][word][0]
		for word in wordInDoc[doc]:
			TF = wordInDoc[doc][word][0] / sizeDoc
			IDF = np.log(nbDocs / wordInCollection[word][0])
			wordInDoc[doc][word][1] = TF*IDF
			wordInCollection[word][1] = IDF
	
	return wordInDoc, wordInCollection
