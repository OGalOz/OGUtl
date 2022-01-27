'''
This file creates a Trie JSON object
given a list of words. All letters are automatically
converted into lower case.
The idea is to store it in as small a way as possible.
'''

import sys, os, logging, json
from typing import List, Dict

def initialize_Trie():
    '''
    "c": -> children (dictionary)
    "w": -> bool if it ends a word
    '''
    T = {
            "c": {},
            "w": False
    }
    return T


def add_word_to_Trie(T, word):
    if len(word) == 0:
        T["w"] = True
    else:
        # word is longer than 0
        first_char = word[0]
        if first_char.lower() in T["c"]:
            add_word_to_Trie(T["c"][first_char.lower()], word[1:])
        else:
            subT = initialize_Trie()
            T["c"][first_char.lower()] = subT
            add_word_to_Trie(T["c"][first_char.lower()], word[1:])


def check_if_word_in_Trie(T, word):
    if len(word) == 0:
        return T["w"]
    else:
        first_char = word[0].lower()
        if first_char in T["c"]:
            return check_if_word_in_Trie(T["c"][first_char], word[1:])
        else:
            return False



def get_all_words_in_Trie(T, crt: str) -> List[str]:
    word_list: List[str] = []
    if T["w"]:
        word_list.append(crt)
    for c in T["c"]:
        word_list += get_all_words_in_Trie(T["c"][c], crt + c)
    return word_list
    





def add_list_of_words_to_new_trie(L: List[str]) -> bool:
    # L is list of words to add 
    T: Dict = initialize_Trie()
    for w in L:
        add_word_to_Trie(T, w)
    return T

def quick_test():
    L: List[str] = ["apple", "app", "banana", "Appalachia"]
    T: Dict = add_list_of_words_to_new_trie(L)
    print(T)
    print(check_if_word_in_Trie(T, "apple"))
    print(check_if_word_in_Trie(T, "APPalachia"))
    print(get_all_words_in_Trie(T, ""))

def main():
    quick_test()


if __name__ == "__main__":
    main()



