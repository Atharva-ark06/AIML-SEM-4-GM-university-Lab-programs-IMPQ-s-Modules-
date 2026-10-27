"""Min-max scale; constant inputs map to zero."""
def minmax_scale(values):
    if not values: raise ValueError("values must not be empty")
    low,high=min(values),max(values)
    if high==low: return [0.0 for _ in values]
    return [(x-low)/(high-low) for x in values]
if __name__ == "__main__": print(minmax_scale([10,20,30]))