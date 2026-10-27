"""Compute expected cost from confusion counts and explicit costs."""
def classification_cost(tp,fp,tn,fn,cost_fp=1,cost_fn=1):
    values=(tp,fp,tn,fn,cost_fp,cost_fn)
    if any(v<0 for v in values): raise ValueError("counts and costs must be non-negative")
    return fp*cost_fp+fn*cost_fn
if __name__ == "__main__": print(classification_cost(80,12,90,18,cost_fp=2,cost_fn=5))