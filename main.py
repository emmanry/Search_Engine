import loadData
import loadRel
import calculateIDF
import calculateTFIDF_doc
import calculateTFIDF_query
import scoreDocs_TFIDF
import scoreDocs_BM25
import analysis

import numpy as np

# List of the words (collection & queries)
words = []

# Load all data
words, occurencesInDoc, occurencesInCollection, occurencesInQueries = loadData.loadData("CISI/CISI.ALL", "CISI/CISI.QRY")

# Calculate IDF for each word of data
wordsIDF = calculateIDF.calculateIDF(len(occurencesInDoc), occurencesInCollection)

# Calculate TFIDF for each word of data
doc_TFIDF, doc_TF = calculateTFIDF_doc.calculateTFIDF_doc(wordsIDF, occurencesInDoc)

# Calculate TF for each word of queries
query_TFIDF = calculateTFIDF_query.calculateTFIDF_query(wordsIDF, occurencesInQueries)

# scoreDocs_Q_TFIDF = scoreDocs_TFIDF.scoreDocs_TFIDF(query_TFIDF['2'], doc_TFIDF)
# scoreDocs_Q_BM25 = scoreDocs_BM25.scoreDocs_BM25(occurencesInQueries['2'], occurencesInDoc, doc_TF, wordsIDF)

# Statistiques
relDocsInQuery = loadRel.loadRel("CISI/CISI.REL")

avg_analysis_TFIDF = (0, 0, 0)
avg_analysis_BM25 = (0, 0, 0)

for query in relDocsInQuery:
    scoreDocs_Q_TFIDF = scoreDocs_TFIDF.scoreDocs_TFIDF(query_TFIDF[query], doc_TFIDF)
    scoreDocs_Q_BM25 = scoreDocs_BM25.scoreDocs_BM25(occurencesInQueries[query], occurencesInDoc, doc_TF, wordsIDF)

    analysis_TFIDF = analysis.analysis(relDocsInQuery[query], scoreDocs_Q_TFIDF)
    analysis_BM25 = analysis.analysis(relDocsInQuery[query], scoreDocs_Q_BM25)

    avg_analysis_TFIDF = [sum(tup) for tup in zip(avg_analysis_TFIDF, analysis_TFIDF)]
    avg_analysis_BM25 = [sum(tup) for tup in zip(avg_analysis_BM25, analysis_BM25)]

print('TFIDF', avg_analysis_TFIDF, '\n BM25', avg_analysis_BM25)

avg_analysis_TFIDF = list(map(lambda x: x / len(relDocsInQuery), avg_analysis_TFIDF))
avg_analysis_BM25 = list(map(lambda x: x / len(relDocsInQuery), avg_analysis_BM25))

print('TFIDF', avg_analysis_TFIDF, '\n BM25', avg_analysis_BM25)

# wordInDoc : { id_doc : {'word' : [occurences_in_doc, 0] ; ...} ; ... }
# wordInCollection : {'word' : [occurences_in_coll, 0] ; ...}

# wordInQueries : { id_query : {'word' : [occurences_in_query, 0] ; ...} ; ... }

# wordInDoc_TFIDF : { id_doc : {'word' : [occurences_in_doc, TF*IDF] ; ...} ; ... }
# wordInCollection_IDF : {'word' : [occurences_in_coll, IDF] ; ...}

# wordInQueries_TFIDF : { id_query : {'word' : [occurences_in_query, TFIDF] ; ...} ; ... }

# Load Data returns :
# Words : ["0", "2", "3", "0", "0", "0", ...]
# OccurencesInDoc : {id_doc : [occurences_in_doc] ; ...}
# OccurencesInCollection : [occurences_in_coll]

# OccurencesInDoc : {id_query : [occurences_in_query] ; ...}

# Calculate TDIF returns :
# { id_doc : [0, 2, 3, 0, 0, 0, ...] ; ...}
# { id_que : [0, 2, 3, 0, 0, 0, ...] ; ...}

# ScoreDocs returns : 
# {id_doc : score ; ...} pour une requete

# joueur : M B C
# pred   : 6 8 3
# verite : 8 0 2
#
# M -> 6 bonnes, B -> 0 et C-> 2 bonnes
# P = 8 (nb bonnes) / 17 (nb total)
# ce que je predis en tant que bon vs ce que je predis en mauvais
# VP, FN vs FP, VN (vrai positif, vrai negatif = ce qui ne se passe pas)
# V = vérité, ce qui s'est vrmt passé
# Precision = VP / VP + FP
# Rappel = VP / VP + FN (est ce qu'il oublie bcp d'élément)
# f mesure = ratio entre précision/ rappel
# Q = prediction 10 
# dans les 10 combien sont dans le V
# si V contient 4 élém, 10 dans Q et 4 de bonne donc Précision = 4/10 (si il se trompe souvent) et Rappel = 4/4 (oublie aucun)
# si V contient 17 élém, 10 dans Q et 4 de bonne donc Précision = 4/10 (si il se trompe souvent) et Rappel = 4/17 (oublie)
