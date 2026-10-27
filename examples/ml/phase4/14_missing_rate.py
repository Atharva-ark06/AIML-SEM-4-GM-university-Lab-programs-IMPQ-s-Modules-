"""Missing-value rate using None as the missing marker."""
def missing_rate(values):
    if not values: raise ValueError("values must not be empty")
    return sum(x is None for x in values)/len(values)
if __name__ == "__main__": print(missing_rate([1,None,3,None]))