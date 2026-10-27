"""Brier score for binary labels and probability forecasts."""
def brier_score(y_true,probabilities):
    if len(y_true)!=len(probabilities): raise ValueError("lengths must match")
    if not y_true: raise ValueError("inputs must not be empty")
    if any(y not in (0,1) for y in y_true): raise ValueError("labels must be 0 or 1")
    if any(not 0<=p<=1 for p in probabilities): raise ValueError("probabilities must be in [0, 1]")
    return sum((y-p)**2 for y,p in zip(y_true,probabilities))/len(y_true)
if __name__ == "__main__": print(brier_score([0,1,1],[0.1,0.8,0.6]))