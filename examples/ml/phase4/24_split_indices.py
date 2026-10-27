"""Deterministic ordered train/test index split for demonstrations."""
def split_indices(n_items,test_fraction=0.2):
    if n_items<2: raise ValueError("at least two items are required")
    if not 0<test_fraction<1: raise ValueError("test_fraction must be between 0 and 1")
    n_test=min(n_items-1,max(1,round(n_items*test_fraction)))
    split=n_items-n_test
    return list(range(split)),list(range(split,n_items))
if __name__ == "__main__": print(split_indices(10,0.2))