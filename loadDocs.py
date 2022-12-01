from removePunctuations import removePunctuations

def loadDocs(filename, words):
	occurencesInDoc = {}
	occurencesInCollection = []
	# Lecture du fichier
	lines = open(filename, encoding="utf-8").readlines()
	
	# Parcours de chaque ligne du fichier
	i = 0
	while(i < len(lines)):
		tokens = lines[i].strip().split()

		# Un document commence par son identifiant représenté par ".I"
		while(((len(tokens) != 0 and tokens[0] != ".I") or len(tokens) == 0)) :
			i=i+1
			if i >= len(lines): 
				return words, occurencesInDoc, occurencesInCollection
			tokens = lines[i].strip().split()

		# Initialisation du document
		idDoc = tokens[1]
		occurencesInDoc[idDoc] = [0]*len(words)
		
		# Passe les lignes inutiles pour arriver au contenu du document
		while(len(tokens) != 0 and tokens[0] != ".W") :
			i=i+1
			tokens = lines[i].strip().split()	
		
		# Récupération de la première ligne du document
		i=i+1
		tokens = lines[i].strip().split()	

		# Parcours de l'ensemble du document
		while(len(tokens) != 0 and tokens[0] != ".X") :
			# Parcours de chaque mot du document
			for j in range(len(tokens)) :
				# Récupération du mot sans ponctuation
				tokens[j] = removePunctuations(tokens[j]) 
				for t in tokens[j]:
					# Mise à jour des variables occurencesInDoc[idDoc] et occurencesInCollection
					if (t in words) : 
						indexWord = words.index(t)

						if (occurencesInDoc[idDoc][indexWord] == 0) :
							occurencesInCollection[indexWord] += 1

						occurencesInDoc[idDoc][indexWord] += 1
					# Ajout du mot dans words, occurencesInDoc[idDoc] et occurencesInCollection
					else : 
						words.append(t)
						occurencesInDoc[idDoc].append(1)
						occurencesInCollection.append(1)
			
			i=i+1
			tokens = lines[i].strip().split()

	return words, occurencesInDoc, occurencesInCollection
