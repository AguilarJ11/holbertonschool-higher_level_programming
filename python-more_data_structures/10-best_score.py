#!/usr/bin/python3

def best_score(a_dictionary):
    score = 0
    for i in a_dictionary:
        if score < a_dictionary.get(i):
            score = a_dictionary.get(i)
    return score
