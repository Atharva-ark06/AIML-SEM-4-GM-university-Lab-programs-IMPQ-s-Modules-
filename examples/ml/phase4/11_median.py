"""Median for a numeric sequence."""
def median(values):
    if not values: raise ValueError("values must not be empty")
    ordered=sorted(values); mid=len(ordered)//2
    return ordered[mid] if len(ordered)%2 else (ordered[mid-1]+ordered[mid])/2
if __name__ == "__main__": print(median([9,1,4,2]))