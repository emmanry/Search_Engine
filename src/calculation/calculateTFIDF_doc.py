import numpy as np

def calculateTFIDF_doc(wordsIDF, occurencesInDoc):
	'''
	Calcule le TFIDF de chaque mot pour chaque document de la collection
	
	@inputs
		- wordsIDF : IDF de chaque mot de la collection ;
		- occurencesInDoc : Dictionnaire qui a pour clé l'id de chaque document et pour valeur le vecteur du nombre d'occurence de chacun des mots du document.

	@output
		- doc_TFIDF : Dictionnaire qui a pour clé l'id de chaque document et pour valeur le vecteur du TFIDF de chacun des mots du document ;
		- doc_TF : Dictionnaire qui a pour clé l'id de chaque document et pour valeur le vecteur du TF de chacun des mots du document.
	'''

	doc_TFIDF = {}
	doc_TF = {}

	for doc in occurencesInDoc:
		sizeDoc = sum(occurencesInDoc[doc])
		wordsTF = (np.array(occurencesInDoc[doc]) / sizeDoc)
		wordsTF = np.concatenate((wordsTF, np.zeros(len(wordsIDF)-len(wordsTF))))
		doc_TF[doc] = wordsTF
		doc_TFIDF[doc] = wordsTF * wordsIDF
	
	return doc_TFIDF, doc_TF
