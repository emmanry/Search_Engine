import loadData
import loadQueries
import calculateTFIDF
import calculateTFIDF_query
import scoreDocs

# Load all data
wordInDoc, wordInCollection = loadData.loadData("CISI/CISI.ALL")

# Load queries
wordInQueries = loadQueries.loadQueries("CISI/CISI.QRY")

# Calculate TFIDF for each word of data
wordInDoc_TFIDF, wordInCollection_IDF = calculateTFIDF.calculateTFIDF(wordInDoc, wordInCollection)

# Calculate TF for each word of queries
wordInQueries_TFIDF = calculateTFIDF_query.calculateTFIDF_query(wordInQueries, wordInCollection_IDF)

scoreDocs_Q = scoreDocs.scoreDocs(wordInQueries_TFIDF["2"], wordInDoc_TFIDF)

print(scoreDocs_Q, "\n", len(scoreDocs_Q))

# a b c
# doc.a doc.b

# dist doc.a,a
# +
# dist doc.b,b