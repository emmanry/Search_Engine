import numpy as np

def calculateIDF(nbDocs, occurencesInCollection):
	'''
	Calcule l'IDF des mots de la collection de documents
	
	@inputs
		- nbDocs : Nombre de documents dans la collection ;
		- occurencesInCollection : Liste du nombre de documents dont le mot à l'indice i apparaît au moins une fois.

	@output
		- Liste des IDF pour chaque mot de la collection
	'''
	return np.log(nbDocs / np.array(occurencesInCollection))
