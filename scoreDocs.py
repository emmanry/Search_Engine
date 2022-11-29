from scipy.spatial import distance
import numpy as np

def scoreDocs(query_TFIDF, doc_TFIDF):
    scoreDocs = {}

    for (idDoc, wordsTFIDF_doc) in doc_TFIDF.items():
        scoreDocs[idDoc] = distance.cosine(wordsTFIDF_doc, query_TFIDF[:len(wordsTFIDF_doc)])
    
    scoreDocs_sorted = dict(sorted(scoreDocs.items(), key=lambda item : item[1])[:10])

    return scoreDocs_sorted
