from loading.removePunctuations import removePunctuations
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

def loadDocs(filename, words):
	'''
	Charge en mémoire les documents
	
	@inputs
		- filename : chemin du document de la collection de documents ;
		- words : Liste vide.
	
	@output
		- words : Liste de tous les mots de la collection de document ;
		- occurencesInDoc : Dictionnaire qui a pour clé l'id de chaque document et pour valeur le vecteur du nombre d'occurence de chacun des mots du document ;
		- occurencesInCollection : Liste du nombre de documents dont le mot à l'indice i apparaît au moins une fois ;
	'''
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
					# Stemming
					t = PorterStemmer().stem(t)
					# Lemmatisation
					#t = WordNetLemmatizer().lemmatize(t)

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
