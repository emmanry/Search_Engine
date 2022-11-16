import loadData
import loadQueries
import calculateTFIDF
import calculateTFIDF_query

# Load all data
wordInDoc, wordInCollection = loadData.loadData("CISI/CISI.ALL")

# Load queries
wordInQueries = loadQueries.loadQueries("CISI/CISI.QRY")

# Calculate TFIDF for each word of data
wordInDoc_TFIDF, wordInCollection_IDF = calculateTFIDF.calculateTFIDF(wordInDoc, wordInCollection)

# Calculate TF for each word of queries
wordInQueries_TF = calculateTFIDF_query.calculateTFIDF_query(wordInCollection_IDF, wordInQueries)

print(wordInQueries_TF)