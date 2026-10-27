"""Root mean squared error."""
from math import sqrt
from importlib import import_module
_mse=import_module("examples.ml.phase4.08_mse").mse
def rmse(actual,predicted): return sqrt(_mse(actual,predicted))
if __name__ == "__main__": print(rmse([3,5,2],[2,5,4]))