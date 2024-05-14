#!/usr/bin/python3

def best_score(a_dictionary):
    best = ""
    for i in a_dictionary:
        if best < a_dictionary.get(i):
            best = i
    return best
