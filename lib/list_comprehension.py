#!/usr/bin/env python3

def return_evens(num_list):
    divisible_by_2 = [num for num in num_list if num % 2 == 0]
    return divisible_by_2
    pass
print(return_evens([1, 2, 3, 4, 5, 6, 7,8,9]))
def make_exclamation(sentence_list):
    empty_list = []
    if not sentence_list:
        return empty_list
    else:
        exclamation_list = [sentence + "!" for sentence in sentence_list]
        return exclamation_list
    pass
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))