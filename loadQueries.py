from removePunctuations import removePunctuations
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


def loadQueries(filename, words):
	occurencesInQuery = {}
	# Lecture du fichier
	lines = open(filename, encoding="utf-8").readlines()

	# Parcours de chaque ligne du fichier
	i = 0
	while(i < len(lines)):
		tokens = lines[i].strip().split()

		# Une requête commence par son identifiant représenté par ".I"
		while(((len(tokens) != 0 and tokens[0] != ".I") or len(tokens) == 0)) :
			i=i+1
			if i >= len(lines): 
				return words, occurencesInQuery
			tokens = lines[i].strip().split()

		# Initialisation de la requête 
		idQuery = tokens[1]
		occurencesInQuery[idQuery] = [0]*len(words)
		
		# Passe les lignes inutiles pour arriver au contenu de la requête
		while((len(tokens) != 0 and tokens[0] != ".W") or len(tokens) == 0) :
			i=i+1
			tokens = lines[i].strip().split()
		
		# Récupération de la première ligne de la requête
		i=i+1
		tokens = lines[i].strip().split()

		# Parcours de l'ensemble de la requête
		while((len(tokens) != 0 and tokens[0] != ".I" and tokens[0] != ".B" and i < len(lines)) or len(tokens) == 0) :
			for j in range(len(tokens)) : 
				# Récupération du mot sans ponctuation
				tokens[j] = removePunctuations(tokens[j]) 

				for t in tokens[j]:
					# Transformation du mot en sa racine
					#t = PorterStemmer().stem(t)
					t = WordNetLemmatizer().lemmatize(t)

					# Mise à jour de occurencesInQuery[idQuery]
					if (t in words) : 
						indexWord = words.index(t)

						occurencesInQuery[idQuery][indexWord] += 1
					# Ajout du mot dans words et occurencesInQuery[idQuery]
					else : 
						words.append(t)
						occurencesInQuery[idQuery].append(1)

			i=i+1
			tokens = lines[i].strip().split()

	return words, occurencesInQuery
