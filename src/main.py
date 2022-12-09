from loading.loadData import loadData
from loading.loadRel import loadRel
from calculation.calculateIDF import calculateIDF
from calculation.calculateTFIDF_doc import calculateTFIDF_doc
from calculation.calculateTFIDF_query import calculateTFIDF_query
from scoring.scoreDocs_TFIDF import scoreDocs_TFIDF
from scoring.scoreDocs_BM25 import scoreDocs_BM25
from analysis import analysis

import numpy as np

# Liste de tous les mots (collection et requêtes)
words = []

# Chargement des données
words, occurencesInDoc, occurencesInCollection, occurencesInQueries = loadData("../CISI/CISI.ALL", "../CISI/CISI.QRY")

# Calcul de l'IDF de chaque mot de la collection
wordsIDF = calculateIDF(len(occurencesInDoc), occurencesInCollection)

# Calcul du TFIDF et du TF de chaque mot pour chaque document
doc_TFIDF, doc_TF = calculateTFIDF_doc(wordsIDF, occurencesInDoc)

# Calcul du TFIDF de chaque mot de chaque requête
query_TFIDF = calculateTFIDF_query(wordsIDF, occurencesInQueries)

scoreDocs_Q_TFIDF = scoreDocs_TFIDF(query_TFIDF['1'], doc_TFIDF)
scoreDocs_Q_BM25 = scoreDocs_BM25(occurencesInQueries['2'], occurencesInDoc, doc_TF, wordsIDF)

################################ STATISTIQUES ################################

# Chargement des résultats
relDocsInQuery = loadRel("../CISI/CISI.REL")

# Initialisation des moyennes des statistiques (précision, rappel, f_mesure) pour TFIDF et BM25
avg_analysis_TFIDF = (0, 0, 0)
avg_analysis_BM25 = (0, 0, 0)

i = 0
print("Calcul 0 sur", len(relDocsInQuery))
for query in relDocsInQuery:
    print("\033[A\033[A")
    i += 1
    print("Calcul", i, "sur", len(relDocsInQuery))
    # Calcul des scores de chaque document pour chaque requêtes pour les 2 méthodes implémentées
    scoreDocs_Q_TFIDF = scoreDocs_TFIDF(query_TFIDF[query], doc_TFIDF)
    scoreDocs_Q_BM25 = scoreDocs_BM25(occurencesInQueries[query], occurencesInDoc, doc_TF, wordsIDF)

    # Calcul des statistiques pour TFIDF et BM25
    analysis_TFIDF = analysis(relDocsInQuery[query], scoreDocs_Q_TFIDF)
    analysis_BM25 = analysis(relDocsInQuery[query], scoreDocs_Q_BM25)

    # Somme des résultats pour chaque requêtes
    avg_analysis_TFIDF = [sum(tup) for tup in zip(avg_analysis_TFIDF, analysis_TFIDF)]
    avg_analysis_BM25 = [sum(tup) for tup in zip(avg_analysis_BM25, analysis_BM25)]

print("\033[A\033[A")

# # Calcul de la moyenne pour chaque statistiques
avg_analysis_TFIDF = list(map(lambda x: x / len(relDocsInQuery), avg_analysis_TFIDF))
avg_analysis_BM25 = list(map(lambda x: x / len(relDocsInQuery), avg_analysis_BM25))

print('TFIDF', avg_analysis_TFIDF, '\n BM25', avg_analysis_BM25)