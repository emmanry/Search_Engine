def loadAllDocs(filename, words):
	lines = open(filename, encoding="utf-8").readlines()
		
	for i in range(len(lines)):
		tokens = lines[i].strip().split()
		
		if (len(tokens) != 0 and tokens[0] == ".W") : 
			
			i=i+1
			tokens = lines[i].strip().split()	

			while(len(tokens) != 0 and tokens[0] != ".X") :

				for j in range(len(tokens)) : 

					if (tokens[j] in words) : 

						words[tokens[j]]+=1

					else : 
						words[tokens[j]]=0

				i=i+1
				tokens = lines[i].strip().split()

	return words


def loadEachDocs(filename, words):

	occurencesInDoc = {}

	lines = open(filename, encoding="utf-8").readlines()
		
	for i in range(len(lines)):
		tokens = lines[i].strip().split()
		
		if (len(tokens) != 0 and tokens[0] == ".I") : 
			idDoc = tokens[1]
			occurencesInDoc[idDoc] = dict.fromkeys(words.keys(),0)
			
			while(len(tokens) != 0 and tokens[0] != ".W") :
				i=i+1
				tokens = lines[i].strip().split()
			
			i=i+1
			tokens = lines[i].strip().split()	

			while(len(tokens) != 0 and tokens[0] != ".X") :

				for j in range(len(tokens)) : 
					occurencesInDoc[idDoc][tokens[j]]+=1

				i=i+1
				tokens = lines[i].strip().split()

	return words, occurencesInDoc

