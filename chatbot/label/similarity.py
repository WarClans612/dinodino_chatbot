#!/usr/bin/env python3
# Developer: Wilbert (wilbert.phen@gmail.com)

import re
import numpy as np

def label_count(inputSegTokenStr):
    pass

def doc_matrix(inputA, inputB):
    countA = label_count(inputA)
    countB = label_count(inputB)

    for keys in countA:
        if keys not in countB:
            countB[keys] = 0
    for keys in countB:
        if keys not in countA:
            countA[keys] = 0

    return countA, countB

def label_cosine_similarity(inputA, inputB):
    vecA, vecB = doc_matrix(inputA, inputB)
    vecA, vecB = np.array(list(vecA.values())), np.array(list(vecB.values()))

    similarity = np.dot(vecA, vecB)
    similarity = np.divide(similarity, np.linalg.norm(vecA) * np.linalg.norm(vecB))

    return similarity

def label_jaccard_similarity(inputA, inputB):
    countA = label_count(inputA)
    countB = label_count(inputB)

    A_tag = set(countA.keys())
    B_tag = set(countB.keys())
    C_tag = A_tag.intersection(B_tag)
    similarity = float(len(C_tag)) / (len(A_tag) + len(B_tag) - len(C_tag))
    return similarity

def score(inputA, inputB):
    weightScoreDict = [
        {'weight': 0.5, 'func': label_cosine_similarity},
        {'weight': 0.5, 'func': label_jaccard_similarity}
    ]
    score = 0
    for item in weightScoreDict:
        score += item['weight'] * item['func'](inputA, inputB)

    return score
