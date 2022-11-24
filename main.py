import loadData
import calculateIDF
import calculateTFIDF_doc
import calculateTFIDF_query
import scoreDocs

# List of the words (collection & queries)
words = []

# Load all data
words, occurencesInDoc, occurencesInCollection, occurencesInQueries = loadData.loadData("CISI/CISI.ALL", "CISI/CISI.QRY")

# Calculate IDF for each word of data
wordsIDF = calculateIDF.calculateIDF(len(occurencesInDoc), occurencesInCollection)

# Calculate TFIDF for each word of data
doc_TFIDF = calculateTFIDF_doc.calculateTFIDF_doc(wordsIDF, occurencesInDoc)

# Calculate TF for each word of queries
query_TFIDF = calculateTFIDF_query.calculateTFIDF_query(wordsIDF, occurencesInQueries)

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
