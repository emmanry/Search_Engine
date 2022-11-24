# TODO : 'word?' != word
def loadQueries(filename, words):
	occurencesInQuery = {}
	lines = open(filename, encoding="utf-8").readlines()
		
	for i in range (len(lines)):
		tokens = lines[i].strip().split()
		
		if (i >= 0) :
			if (len(tokens) != 0 and tokens[0] == ".I") : 
				idQuery = tokens[1]
				occurencesInQuery[idQuery] = [0]*len(words)
				
				while(len(tokens) != 0 and tokens[0] != ".W") :
					i=i+1
					tokens = lines[i].strip().split()
				
				i=i+1
				tokens = lines[i].strip().split()	

				while(len(tokens) != 0 and tokens[0] != ".I" and tokens[0] != ".B") :
					for j in range(len(tokens)) : 
						if (tokens[j] in words) : 
							indexWord = words.index(tokens[j])

							occurencesInQuery[idQuery][indexWord] += 1
						else : 
							words.append(tokens[j])
							occurencesInQuery[idQuery].append(1)

					i=i+1
					tokens = lines[i].strip().split()

	return words, occurencesInQuery
