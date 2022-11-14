from scipy.spatial import distance
import numpy as np



def load(filename):
	wordInDoc = {}
	wordInCollection = {}
	lines = open(filename, encoding="utf-8").readlines()
		
	for i in len(lines):
		tokens = lines[i].strip().split()
		
		if (i > 0) :
			if (tokens[0] == ".I") : 
				idDoc = tokens[1]
				wordInDoc[idDoc] = {}
				
				
				while(tokens[0] != ".W") :
					i=i+1
					tokens = lines[i].strip().split()
				
				i=i+1
				tokens = lines[i].strip().split()	
				
				while(tokens[0] != ".X") :
				
					for j in len(tokens) : 
						if (tokens[j] in wordInDoc[idDoc].keys()) :
							wordInDoc[idDoc][tokens[j]][0] += 1
						else :
							wordInDoc[idDoc][tokens[j]] = [1, 0]
							
							if (tokens[j] in wordInCollection.keys()) :
								wordInCollection[tokens[j]] += 1
							else :
								wordInCollection[tokens[j]] = 1

					i=i+1
					tokens = lines[i++].strip().split()	
			
	
			
	return 
	

