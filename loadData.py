def loadData(filename):
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
								wordInCollection[tokens[j]][0] += 1
							else :
								wordInCollection[tokens[j]] = [1, 0]

					i=i+1
					tokens = lines[i].strip().split()

	return wordInDoc, wordInCollection
