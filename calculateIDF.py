import numpy as np

def calculateIDF(nbDocs, occurencesInCollection):
	return np.log(nbDocs / np.array(occurencesInCollection))
