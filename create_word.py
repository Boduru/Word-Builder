from pickle import load
from random import choice
import numpy as np
from pprint import pprint


def load_model(filename):
    """Load model from file"""

    with open(filename, "rb") as f:
        return load(f)


def get_next_letter(choices, weights):
    """Get next letter by weighted random choice"""

    return np.random.choice(choices, p=weights)


def extract_choices_weights(letter):
    """Get choices and weights in separeted lists"""

    return list(zip(*list(model[letter].items())))


def flatten(weights):
    """Make probabilities summ to 1"""

    return [w / sum(weights) for w in weights]


def get_end_letter(bigram):
    """Search end letter by simulating next bigram apparition"""

    supposed_new_letter = get_next_letter(*extract_choices_weights(bigram))
    bigrams, weights = extract_choices_weights("?")

    pretendents, pretendents_weights = get_pretendents(bigrams, weights, supposed_new_letter)
    flatten_weights = flatten(pretendents_weights)

    return get_next_letter(pretendents, flatten_weights)


def get_pretendents(bigrams, weights, supposed_new_letter):
    """Get all possible next bigram for the given letter"""

    pretendents = []
    pretendents_weights = []

    for i, k in enumerate(bigrams):
        if k[0] == supposed_new_letter:
            pretendents.append(k)
            pretendents_weights.append(weights[i])

    return pretendents, pretendents_weights


def build_words(n=10, l=6):
    """Build n words of l lenght"""

    words = []

    for j in range(n):
        words.append(create(l))

    return words


def create(l):
    """Create word with given lenght"""

    word = ""

    while len(word) < l:
        if len(word) == l-2:
            new_letter = get_end_letter(word[-2:])
        else:
            if len(word) == 0:
                pattern = "!"
            elif len(word) < l-1:
                pattern = word[-2:]

            new_letter = get_next_letter(*extract_choices_weights(pattern))

        word += new_letter

    return word


if __name__ == "__main__":
    # Dictionnary containing all the transitions probabilities
    # ! stands for: start of the word
    # ? stands for: end of the word
    model = load_model("model.pickle")

    words = build_words(5, 6)

    pprint(words)