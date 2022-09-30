#!/usr/bin/python3
def best_score(a_dict):
    if a_dict is None  or a_dict == {}:
        return None
    maxA = max(a_dict.values())
    for key in a_dict:
        if maxA == a_dict[key]:
            return key
