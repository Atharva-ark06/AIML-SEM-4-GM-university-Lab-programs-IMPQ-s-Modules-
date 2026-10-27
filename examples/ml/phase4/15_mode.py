"""Most frequent value with deterministic tie-breaking."""
from collections import Counter
def mode(values):
    if not values: raise ValueError("values must not be empty")
    counts=Counter(values)
    return max(counts,key=lambda value:(counts[value],str(value)))
if __name__ == "__main__": print(mode(["blue","red","blue","green"]))