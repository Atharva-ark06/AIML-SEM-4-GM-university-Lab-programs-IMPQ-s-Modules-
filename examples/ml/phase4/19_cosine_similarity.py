"""Cosine similarity for non-zero numeric vectors."""
from math import sqrt
def cosine_similarity(a,b):
    if len(a)!=len(b): raise ValueError("vector lengths must match")
    na=sqrt(sum(x*x for x in a)); nb=sqrt(sum(x*x for x in b))
    if na==0 or nb==0: raise ValueError("zero vector has undefined cosine similarity")
    return sum(x*y for x,y in zip(a,b))/(na*nb)
if __name__ == "__main__": print(cosine_similarity([1,0],[0.5,0.5]))