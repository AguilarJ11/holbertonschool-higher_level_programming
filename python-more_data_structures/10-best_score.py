#!/usr/bin/python3

def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    elif a_dictionary is None:
        return None
    best = ""
    score = 0
    for i in a_dictionary:
        if score < a_dictionary.get(i):
            score = a_dictionary.get(i)
            best = i
    return best
