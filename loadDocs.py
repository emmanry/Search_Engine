import removePunctuations

def loadDocs(filename, words):
	occurencesInDoc = {}
	occurencesInCollection = []
	# Lecture du fichier
	lines = open(filename, encoding="utf-8").readlines()
	
	# Parcours de chaque ligne du fichier
	for i in range(len(lines)):
		tokens = lines[i].strip().split()
		
		# Un document commence par son identifiant représenté par ".I"
		if (len(tokens) != 0 and tokens[0] == ".I") : 
			# Initialisation du document
			idDoc = tokens[1]
			occurencesInDoc[idDoc] = [0]*len(words)
			
			# Passe les lignes inutiles pour arriver au contenu du document
			while(len(tokens) != 0 and tokens[0] != ".W") :
				i=i+1
				tokens = lines[i].strip().split()	
			
			i=i+1
			tokens = lines[i].strip().split()	

			# Parcours de l'ensemble du document
			while(len(tokens) != 0 and tokens[0] != ".X") :

				# Parcours de chaque mot du document
				for j in range(len(tokens)) :
					# Récupération du mot sans ponctuation
					tokens[j] = removePunctuations.removePunctuations(tokens[j]) 
					# Mise à jour des variables occurencesInDoc[idDoc] et occurencesInCollection
					if (tokens[j] in words) : 
						indexWord = words.index(tokens[j])

						if (occurencesInDoc[idDoc][indexWord] == 0) :
							occurencesInCollection[indexWord] += 1

						occurencesInDoc[idDoc][indexWord] += 1
					# Ajout du mot dans words, occurencesInDoc[idDoc] et occurencesInCollection
					else : 
						words.append(tokens[j])
						occurencesInDoc[idDoc].append(1)
						occurencesInCollection.append(1)

				i=i+1
				tokens = lines[i].strip().split()

	return words, occurencesInDoc, occurencesInCollection
