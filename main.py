from scipy.spatial import distance
import numpy as np

# { id_doc: { 'mot' : [nb_de_fois_dans_le_doc, TFIDF] ; ... } ; ...}
# { 'This' : nb_total_de_doc_dans_lequel_il_apparait }

def load(filename):
	wordInDoc = {}
	wordInCollection = {}
	lines = open(filename, encoding="utf-8").readlines()
		
	for i in range (len(lines)):
		tokens = lines[i].strip().split()
		
		if (i >= 0) :
			if (len(tokens) != 0 and tokens[0] == ".I") : 
				idDoc = tokens[1]
				wordInDoc[idDoc] = {}
				
				
				while(len(tokens) != 0 and tokens[0] != ".W") :
					i=i+1
					tokens = lines[i].strip().split()
				
				i=i+1
				tokens = lines[i].strip().split()	

				while(len(tokens) != 0 and tokens[0] != ".X") :
				
					for j in range (len(tokens)) : 
						if (tokens[j] in wordInDoc[idDoc].keys()) :
							wordInDoc[idDoc][tokens[j]][0] += 1
						else :
							wordInDoc[idDoc][tokens[j]] = [1, 0]
							
							if (tokens[j] in wordInCollection.keys()) :
								wordInCollection[tokens[j]] += 1
							else :
								wordInCollection[tokens[j]] = 1

					i=i+1
					tokens = lines[i].strip().split()
	return wordInDoc, wordInCollection

def calculateTFIDF(wordInDoc, wordInCollection):

	nbDocs = len(wordInDoc)
	
	for doc in wordInDoc:
		sizeDoc = 0
		for word in wordInDoc[doc]:
			sizeDoc += wordInDoc[doc][word][0]
		for word in wordInDoc[doc]:
			TF = wordInDoc[doc][word][0] / sizeDoc
			IDF = np.log(nbDocs / wordInCollection[word])
			wordInDoc[doc][word][1] = TF*IDF
	
	return wordInDoc

wordInDoc, wordInCollection = load("/home/emmanourry/Documents/ET5/Extraction info-texte/Projet/Search_Engine/CISI/CISI.ALL")

wordInDoc_TFIDF = calculateTFIDF(wordInDoc, wordInCollection)

print(wordInDoc_TFIDF)