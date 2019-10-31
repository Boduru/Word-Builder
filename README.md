# Word-builder Description
A Python program that can create new words on any European language

## Method
Algorithm based on Markov Chains transition probabilities

## First step
Creation of the letter transition probabilities matrix, that gives the potential next letter with weights for the given bigram.

## Second step
Create words using the matrix and random weighted choices 

## Parameters
model = matrix of transition probabilities\
n = number of words wanted to be generated\
l = lenght of the words to generate
