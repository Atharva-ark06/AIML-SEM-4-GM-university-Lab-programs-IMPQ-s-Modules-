"""Mean absolute error for numeric sequences."""
def mae(actual,predicted):
    if len(actual)!=len(predicted): raise ValueError("lengths must match")
    if not actual: raise ValueError("inputs must not be empty")
    return sum(abs(a-p) for a,p in zip(actual,predicted))/len(actual)
if __name__ == "__main__": print(mae([3,5,2],[2,5,4]))