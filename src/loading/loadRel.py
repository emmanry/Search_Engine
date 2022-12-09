def loadRel(filename):
    '''
	Charge en mémoire les résultats
	
	@inputs
		- filename : chemin du document des résultats.
	
	@output
		- relDocsInQuery : Dictionnaire ayant pour clé l'id d'une requête et pour valeur la liste des documents pertinents (résultats théoriques).
    '''
    
    relDocsInQuery = {}
	# Lecture du fichier
    lines = open(filename, encoding="utf-8").readlines()

	# Parcours de chaque ligne du fichier
    for i in range(len(lines)):
        tokens = lines[i].strip().split()

        # Création et mise à jour de la liste relDocsInQuery[idQuery]
        idQuery = tokens[0]
        if idQuery in relDocsInQuery.keys():
            relDocsInQuery[idQuery].append(tokens[1])
        else :
            relDocsInQuery[idQuery] = [tokens[1]]

    return relDocsInQuery