"""Standardize values with training-set statistics."""
def standardize(values,mean,std):
    if std<=0: raise ValueError("std must be positive")
    return [(x-mean)/std for x in values]
if __name__ == "__main__": print(standardize([2,4,6],4,2))