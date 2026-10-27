"""Manhattan distance between numeric vectors."""
def manhattan(a,b):
    if len(a)!=len(b): raise ValueError("vector lengths must match")
    return sum(abs(x-y) for x,y in zip(a,b))
if __name__ == "__main__": print(manhattan([1,2],[4,6]))