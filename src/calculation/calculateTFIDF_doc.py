import numpy as np

def calculateTFIDF_doc(wordsIDF, occurencesInDoc):
	doc_TFIDF = {}
	doc_TF = {}

	for doc in occurencesInDoc:
		sizeDoc = sum(occurencesInDoc[doc])
		wordsTF = (np.array(occurencesInDoc[doc]) / sizeDoc)
		wordsTF = np.concatenate((wordsTF, np.zeros(len(wordsIDF)-len(wordsTF))))
		doc_TF[doc] = wordsTF
		doc_TFIDF[doc] = wordsTF * wordsIDF
	
	return doc_TFIDF, doc_TF
