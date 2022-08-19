# Word Builder
Program that can create new words in any european language of the desired length.

## Method
Algorithm based on Markov Chains Transition Probabilities

## Procedure
1. Creation of the transition matrix
2. Add letter to word randomly using the matrix and random weighted choices 

## Parameters
model: matrix of transition probabilities\
n: number of words wanted to be generated\
l: lenght of the words to generate

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
