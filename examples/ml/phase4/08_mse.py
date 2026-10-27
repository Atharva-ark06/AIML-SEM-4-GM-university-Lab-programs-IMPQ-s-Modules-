"""Mean squared error for numeric sequences."""
def mse(actual,predicted):
    if len(actual)!=len(predicted): raise ValueError("lengths must match")
    if not actual: raise ValueError("inputs must not be empty")
    return sum((a-p)**2 for a,p in zip(actual,predicted))/len(actual)
if __name__ == "__main__": print(mse([3,5,2],[2,5,4]))