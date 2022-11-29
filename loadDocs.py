def loadDocs(filename, words):
	occurencesInDoc = {}
	occurencesInCollection = []
	lines = open(filename, encoding="utf-8").readlines()
		
	for i in range(len(lines)):
		tokens = lines[i].strip().split()
		
		if (len(tokens) != 0 and tokens[0] == ".I") : 
			idDoc = tokens[1]
			occurencesInDoc[idDoc] = [0]*len(words)
			
			while(len(tokens) != 0 and tokens[0] != ".W") :
				i=i+1
			
			i=i+1
			tokens = lines[i].strip().split()	

			while(len(tokens) != 0 and tokens[0] != ".X") :

				for j in range(len(tokens)) : 
					if (tokens[j] in words) : 
						indexWord = words.index(tokens[j])

						if (occurencesInDoc[idDoc][indexWord] == 0) :
							occurencesInCollection[indexWord] += 1

						occurencesInDoc[idDoc][indexWord] += 1
					else : 
						words.append(tokens[j])
						occurencesInDoc[idDoc].append(1)
						occurencesInCollection.append(1)

				i=i+1
				tokens = lines[i].strip().split()

	return words, occurencesInDoc, occurencesInCollection
