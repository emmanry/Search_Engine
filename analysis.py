import numpy as np

def analysis(relQuery, scoreDocs):

    TP = len(np.intersect1d(relQuery, list(scoreDocs.keys())))
    FP = len(scoreDocs) - TP
    FN = len(relQuery) - TP

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f_mesure = 2 * (precision*recall) / (precision + recall + 1e-13)

    return precision, recall, f_mesure