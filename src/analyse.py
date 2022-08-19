"""
Coding utf-8
Python 3.X
Author: Jim Pavan
Tags: Word analyser, statistics builder

"""


import pickle as pkl
import pandas as pd
import re
import unidecode as uni
from pprint import pprint


def preprocessing(words):
    """Preprocess datas, remove accents, spaces, uppercases"""

    preprocessed_words = []

    for word in words:
        word = uni.unidecode(word)
        word = re.sub(r'[^\w\s\d]', '', word)

        preprocessed_words.append(word.lower())

    return preprocessed_words


def compute(dataset, table):
    """Analyse datas from the dataset, count occurrences"""

    for word in dataset:
        for i, letter in enumerate(word):
            if i == 0 and i < len(word) - 1:
                table["!"][letter + word[i+1]] += 1
            elif i < len(word) - 2:
                table[letter + word[i+1]][word[i+2]] += 1
            elif i < len(word) - 1:
                table["?"][letter + word[i+1]] += 1

    return table


def calculate(table):
    """Calculate table statistics"""

    statistics = create_bigrams_dictionnary(bigrams, letters)

    for letter, items in table.items():
        total = sum(items.values())

        for next_letter, val in items.items():
            if total:
                statistics[letter][next_letter] = val / total

    return statistics


def get_all_letters(dataset):
    """Create a set of all letters"""

    letters = set()

    [letters.update(*word) for word in dataset]

    return letters


def get_all_bigrams(dataset):
    """Create a set containing all the bigrams"""

    bi = set()

    for word in dataset:
        for i in range(len(word)):
            if i + 1 < len(word):
                bi.update([word[i] + word[i+1]])

    return bi


def create_bigrams_dictionnary(bigrams, letters):
    """Create letter dictionnary, 
    ! stands for: start,
    ? stands for: end"""

    res = {}
    for key in bigrams:
        res[key] = create_sub_dict(letters)

    res["!"] = create_sub_dict(get_all_bigrams(dataset))
    res["?"] = create_sub_dict(get_all_bigrams(dataset))

    return res


def create_sub_dict(letters):
    """Sub dictionnary"""

    return dict.fromkeys(list(letters), 0)


def save_model(filename):
    """Save model"""

    with open(filename, "wb") as f:
        pkl.dump(statistics, f)


if __name__ == "__main__":
    # Import datas and create Dataset
    dataset = pd.read_csv("french.csv", encoding="utf-8-sig")

    # Initialize datas and create structures
    dataset = preprocessing(dataset["Words"])
    letters = get_all_letters(dataset)
    bigrams = get_all_bigrams(dataset)
    table = create_bigrams_dictionnary(bigrams, letters)

    # Process calculation
    table = compute(dataset, table)
    statistics = calculate(table)

    # Save the model into file through pickle
    save_model("model.pickle")