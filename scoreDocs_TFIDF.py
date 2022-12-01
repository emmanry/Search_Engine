from scipy.spatial import distance

def scoreDocs_TFIDF(query_TFIDF, doc_TFIDF):
    scoreDocs = {}

    for (idDoc, wordsTFIDF_doc) in doc_TFIDF.items():
        scoreDocs[idDoc] = distance.cosine(wordsTFIDF_doc, query_TFIDF)
    
    scoreDocs_sorted = dict(sorted(scoreDocs.items(), key=lambda item : item[1])[:10])

    return scoreDocs_sorted
