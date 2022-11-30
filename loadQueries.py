import removePunctuations

def loadQueries(filename, words):
	occurencesInQuery = {}
	# Lecture du fichier
	lines = open(filename, encoding="utf-8").readlines()

	# Parcours de chaque ligne du fichier
	for i in range (len(lines)):
		tokens = lines[i].strip().split()

		# Une requête commence par son identifiant représenté par ".I"
		if (len(tokens) != 0 and tokens[0] == ".I") :
			# Initialisation de la requête 
			idQuery = tokens[1]
			occurencesInQuery[idQuery] = [0]*len(words)
			
			# Passe les lignes inutiles pour arriver au contenu de la requête
			while(len(tokens) != 0 and tokens[0] != ".W") :
				i=i+1
				tokens = lines[i].strip().split()
			
			i=i+1
			tokens = lines[i].strip().split()

			# Parcours de l'ensemble de la requête
			while(len(tokens) != 0 and tokens[0] != ".I" and tokens[0] != ".B") :
				for j in range(len(tokens)) : 
					# Récupération du mot sans ponctuation
					tokens[j] = removePunctuations.removePunctuations(tokens[j]) 
					
					# Mise à jour de occurencesInQuery[idQuery]
					if (tokens[j] in words) : 
						indexWord = words.index(tokens[j])

						occurencesInQuery[idQuery][indexWord] += 1
					# Ajout du mot dans words et occurencesInQuery[idQuery]
					else : 
						words.append(tokens[j])
						occurencesInQuery[idQuery].append(1)

				i=i+1
				tokens = lines[i].strip().split()

	return words, occurencesInQuery
