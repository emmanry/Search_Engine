import loadData
import calculateIDF
import calculateTFIDF_doc
import calculateTFIDF_query
import scoreDocs

# List of the words (collection & queries)
words = []

# Load all data
words, occurencesInDoc, occurencesInCollection, occurencesInQueries = loadData.loadData("CISI/CISI.ALL", "CISI/CISI.QRY")

print('words :', len(words))

# Calculate IDF for each word of data
wordsIDF = calculateIDF.calculateIDF(len(occurencesInDoc), occurencesInCollection)

print('wordsIDF :', len(wordsIDF))

# Calculate TFIDF for each word of data
doc_TFIDF, doc_TF = calculateTFIDF_doc.calculateTFIDF_doc(wordsIDF, occurencesInDoc)

print('doc :', len(doc_TFIDF['1']))

# Calculate TF for each word of queries
query_TFIDF = calculateTFIDF_query.calculateTFIDF_query(wordsIDF, occurencesInQueries)

print('qry :', len(query_TFIDF['1']))

scoreDocs_Q = scoreDocs.scoreDocs(query_TFIDF["2"], doc_TFIDF)

print(scoreDocs_Q.keys())

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
# res    : 8 0 2
#
# M -> 6 bonnes, B -> 0 et C-> 2 bonnes
# P = 8 (nb bonnes) / 17 (nb total)
# ce que je predis en tant que bon vs ce que je predis en mauvais
# VP, FN vs FP, VN (vrai positif, vrai negatif = ce qui ne se passe pas)
# V = vérité, ce qui s'est vrmt passé
# Precision = VP / VP + FN 
# Rappel = VP / VP + FP (est ce qu'il oublie bcp d'élément)
# f mesure = ratio entre précision/ rappel
# Q = prediction 10 
# dans les 10 combien sont dans le V
# si V contient 4 élém, 10 dans Q et 4 de bonne donc Précision = 4/10 (si il se trompe souvent) et Rappel = 4/4 (oublie aucun)
# si V contient 17 élém, 10 dans Q et 4 de bonne donc Précision = 4/10 (si il se trompe souvent) et Rappel = 4/17 (oublie)
