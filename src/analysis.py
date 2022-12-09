import numpy as np

def analysis(relQuery, scoreDocs):
    '''
    Calcule les grandeurs pour l'analyse des résultats
	
	@inputs
		- relQuery : Liste des documents théoriques associés à une requête ;
		- scoreDocs : Dictionnaire ayant pour clé l'id d'un document et pour valeur son score (Taille 10).
	
	@output
		- TP : Nombre de vrais positifs ;
        - FP : Nombre de faux positifs ;
        - FN : Nombre de faux négatifs.
    '''
    TP = len(np.intersect1d(relQuery, list(scoreDocs.keys())))
    FP = len(scoreDocs) - TP
    FN = len(relQuery) - TP

    return TP, FP, FN