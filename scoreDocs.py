from scipy.spatial import distance
import numpy as np

def scoreDocs(wordInQuery, wordInDoc):
    scoreDocs = {}
    threshold = 0.35

    for (idDoc, wordDoc) in wordInDoc.items():
        score = 0

        for (word, valueQuery) in wordInQuery.items():
            if (word in wordDoc.keys()):
                score += distance.cosine([wordDoc[word][1]], [valueQuery[1]])**2
            else :
                score += valueQuery[1]

        scoreDocs[idDoc] = np.sqrt(score/len(wordInQuery))

    scoreDocs_selected = {}
    for doc in scoreDocs:
        if (scoreDocs[doc] < threshold) :
            scoreDocs_selected[doc] = scoreDocs[doc]

    return dict(sorted(scoreDocs_selected.items(), key=lambda item : item[1]))
