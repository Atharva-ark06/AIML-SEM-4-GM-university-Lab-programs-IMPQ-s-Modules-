"""Arithmetic mean with empty-input validation."""
def mean(values):
    if not values: raise ValueError("values must not be empty")
    return sum(values)/len(values)
if __name__ == "__main__": print(mean([2,4,6,8]))