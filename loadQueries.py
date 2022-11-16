def loadQueries(filename):
	wordInQuery = {}
	lines = open(filename, encoding="utf-8").readlines()
		
	for i in range (len(lines)):
		tokens = lines[i].strip().split()
		
		if (i >= 0) :
			if (len(tokens) != 0 and tokens[0] == ".I") : 
				idQuery = tokens[1]
				wordInQuery[idQuery] = {}
				
				while(len(tokens) != 0 and tokens[0] != ".W") :
					i=i+1
					tokens = lines[i].strip().split()
				
				i=i+1
				tokens = lines[i].strip().split()	

				while(len(tokens) != 0 and tokens[0] != ".I" and tokens[0] != ".B") :
					for j in range (len(tokens)) : 
						if (tokens[j] in wordInQuery[idQuery].keys()) :
							wordInQuery[idQuery][tokens[j]][0] += 1
						else :
							wordInQuery[idQuery][tokens[j]] = [1, 0]

					i=i+1
					tokens = lines[i].strip().split()

	return wordInQuery
