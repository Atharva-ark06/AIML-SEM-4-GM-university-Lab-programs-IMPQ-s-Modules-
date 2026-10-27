"""Check whether two index partitions overlap."""
def has_overlap(train_indices,test_indices):
    return bool(set(train_indices).intersection(test_indices))
if __name__ == "__main__": print(has_overlap([0,1,2],[3,4]))