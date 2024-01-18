#!/usr/bin/env python3

def return_evens(num_list):
    pass
    
    even_numbers = [n for n in num_list if n%2 == 0]
    return even_numbers
    # for n in num_list:
    #     even_numbers = list()
    #     if n%2 == 0:
    #         even_numbers.append(n)
    #     else:
    #         return even_numbers

def make_exclamation(sentence_list):
    pass
    exclaim_word = [(n + "!") for n in sentence_list]
    # if len(sentence_list) == 0:
    #     return []
    # elif len(sentence_list) > 0:
    #     for n in sentence_list:
    #         exclaim_word = n + "!"
    return exclaim_word
