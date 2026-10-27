"""Pair each observation with its absolute prediction error."""
def absolute_errors(actual,predicted):
    if len(actual)!=len(predicted): raise ValueError("lengths must match")
    return [abs(a-p) for a,p in zip(actual,predicted)]
if __name__ == "__main__": print(absolute_errors([4,7,10],[5,5,12]))