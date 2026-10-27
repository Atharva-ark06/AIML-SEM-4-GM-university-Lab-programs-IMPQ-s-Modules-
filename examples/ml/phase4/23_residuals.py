"""Residuals are actual values minus predictions."""
def residuals(actual,predicted):
    if len(actual)!=len(predicted): raise ValueError("lengths must match")
    return [a-p for a,p in zip(actual,predicted)]
if __name__ == "__main__": print(residuals([10,12,8],[9,13,8]))