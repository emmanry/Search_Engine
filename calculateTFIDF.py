import numpy as np

def calculateTFIDF(wordInDoc, wordInCollection):

	###############################################################################################
	# Function that calculates the TFIDF of a word in specific document							  #
	# Parameters 																				  #
	#	- wordInDoc        : The dictionnary of all documents of the collection, 				  #
	#				         the value of a document d is an other dictionnary of all its words,  #
	# 				         the value of a word w in the document d is an array of 			  #
	# 				         two elements : [nb of occurences of the w in d, 0] 				  #
	#   - wordInCollection : The dictionnary of all words in the collection,					  #
	#						 the value of w is an array of two elements : 						  #
	# 						 [nb of occurences w in the collection, 0]							  #
	# Returns																					  #
	#	- wordInDoc        : The dictionnary of all documents of the collection, 				  #
	#				         the value of a document d is an other dictionnary of all its words,  #
	# 				         the value of a word w in the document d is an array of               #
	# 				         two elements : [nb of occurences of the w in d, TFIDF of w in d]     #
	#   - wordInCollection : The dictionnary of all words in the collection,					  #
	#						 the value of w is an array of two elements : 						  #
	# 						 [nb of occurences w in the collection, IDF of the w]                 #
	###############################################################################################
	
	# Number of documents in the collection
	nbDocs = len(wordInDoc)
	
	for doc in wordInDoc:
		sizeDoc = 0
		for word in wordInDoc[doc]:
			# Number of words in the document doc
			sizeDoc += wordInDoc[doc][word][0]
		for word in wordInDoc[doc]:
			# Calculate TF and IDF of word in doc
			TF = wordInDoc[doc][word][0] / sizeDoc
			IDF = np.log(nbDocs / wordInCollection[word][0])
			# Update the TFIDF in wordInDoc
			wordInDoc[doc][word][1] = TF*IDF
			# Update the IDF in wordInDoc
			wordInCollection[word][1] = IDF
	
	return wordInDoc, wordInCollection
