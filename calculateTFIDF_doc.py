import numpy as np

def calculateTFIDF_doc(wordsIDF, occurencesInDoc):
	doc_TFIDF = {}

	for doc in occurencesInDoc:
		sizeDoc = sum(occurencesInDoc[doc])
		wordsTF = (np.array(occurencesInDoc[doc]) / sizeDoc)
		wordsTF = np.concatenate((wordsTF, np.zeros(len(wordsIDF)-len(wordsTF))))
		doc_TFIDF[doc] = wordsTF * wordsIDF
	
	return doc_TFIDF
