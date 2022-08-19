# Word Builder
Program that can create new words in any european language of the desired length.

## Method
Algorithm based on Markov Chains Transition Probabilities

## Procedure
1. Creation of the transition matrix
2. Add letter to word randomly using the matrix and random weighted choice

## Parameters
model: matrix of transition probabilities\
n: number of words wanted to be generated\
l: lenght of the words to generate

## Extend
In order to create words from another language, you need to get a dictionary, and use it as the main word source. The words generated will be based on the words examined during the analysis process on the dictionary.

## Run
```
python analyse.py
```
Next
```
python create_word.py
```

## Requirements
- Python 3.X.X
- Pandas
