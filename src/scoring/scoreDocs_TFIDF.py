from scipy.spatial import distance

def scoreDocs_TFIDF(query_TFIDF, doc_TFIDF):
    '''
    Calcule les scores selon TFIDF de chaque documents pour une requête
	
	@inputs
		- query_TFIDF : Dictionnaire qui a pour clé l'id de chaque requête et pour valeur le vecteur du TFIDF de chacun des mots de la requête ;
		- doc_TFIDF : Dictionnaire qui a pour clé l'id de chaque document et pour valeur le vecteur du TFIDF de chacun des mots du document.
	
	@output
		- scoreDocs_sorted : Dictionnaire ayant pour clé l'id d'un document et pour valeur son score (ressort les 10 meilleurs).
    '''
    scoreDocs = {}

    for (idDoc, wordsTFIDF_doc) in doc_TFIDF.items():
        scoreDocs[idDoc] = distance.cosine(wordsTFIDF_doc, query_TFIDF)
    
    scoreDocs_sorted = dict(sorted(scoreDocs.items(), key=lambda item : item[1])[:10])

    return scoreDocs_sorted
