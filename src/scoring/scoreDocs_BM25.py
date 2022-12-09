import numpy as np

def scoreDocs_BM25(wordsInQuery, occurencesInDoc, doc_TF, wordsIDF):
    
    # Calcul de la longueur moyenne des documents dans la collection
    avgdl = 0
    nbDocs = len(occurencesInDoc)
    for doc in occurencesInDoc:
        avgdl += sum(occurencesInDoc[doc])
    avgdl /= nbDocs

    # Paramètres constants
    k = 1.2 # doit être compris entre 1.2 et 2.0 inclus
    b = 0.5

    # Calcul du score BM25
    scoreDocs = {}
    for (idDoc, wordsInDoc) in occurencesInDoc.items():
        scoreDocs[idDoc] = 0
        for i in np.flatnonzero(wordsInQuery):
            if len(doc_TF[idDoc]) > i:
                scoreDocs[idDoc] += (wordsIDF[i] * doc_TF[idDoc][i] * (k+1) / (doc_TF[idDoc][i] + k*(1 - b + b*(sum(wordsInDoc)/avgdl)))) * wordsInQuery[i]

    # Tri et sélection des 10 premiers
    scoreDocs_sorted = dict(sorted(scoreDocs.items(), key=lambda item : item[1])[-10:])

    return scoreDocs_sorted