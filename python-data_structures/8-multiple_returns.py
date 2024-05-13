#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple = (0,None)
        return tuple
    tuple = (len(sentence), sentence[0])
    return tuple
