import numpy as np

def calculateTFIDF_query(wordInQuery, wordInCollection):

	###############################################################################################
	# Function that calculates the TFIDF of a word in specific document							  #
	# Parameters 																				  #
	#	- wordInQuery        : The dictionnary of all queries of the collection, 				  #
	#				         the value of a query q is an other dictionnary of all its words,     #
	# 				         the value of a word w in the query q is an array of 			      #
	# 				         two elements : [nb of occurences of the w in q, 0] 				  #
	#   - wordInCollection : The dictionnary of all words in the collection,					  #
	#						 the value of w is an array of two elements : 						  #
	# 						 [nb of occurences w in the collection, IDF of the w]							  #
	# Returns																					  #
	#	- wordInQuery        : The dictionnary of all queries of the collection, 				  #
	#				         the value of a query q is an other dictionnary of all its words,     #
	# 				         the value of a word w in the query q is an array of 			      #
	# 				         two elements : [nb of occurences of the w in q, TFIDF of w in q] 	  #			  #
	###############################################################################################

	for query in wordInQuery:
		sizeQuery = 0
		for word in wordInQuery[query]:
			# Number of words in the query query
			sizeQuery += wordInQuery[query][word][0]
		for word in wordInQuery[query]:
			# Calculate TF of word in query
			TF = wordInQuery[query][word][0] / sizeQuery
			# If the word exists in the collection of documents, update the TFIDF in wordInQuery
			if (word in wordInCollection.keys()):
				wordInQuery[query][word][1] = TF * wordInCollection[word][1]
			else :
				wordInQuery[query][word][1] = TF * 0 #TODO : Comment le gérer ??
	
	return wordInQuery
