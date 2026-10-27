"""Euclidean distance between numeric vectors."""
from math import sqrt
def euclidean(a,b):
    if len(a)!=len(b): raise ValueError("vector lengths must match")
    return sqrt(sum((x-y)**2 for x,y in zip(a,b)))
if __name__ == "__main__": print(euclidean([1,2],[4,6]))