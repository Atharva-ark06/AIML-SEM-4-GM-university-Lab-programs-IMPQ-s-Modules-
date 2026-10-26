"""Column-wise missing-value summary and numeric mean imputation."""
from math import isnan

def missing_count(values: list[float | None]) -> int:
    return sum(value is None or (isinstance(value, float) and isnan(value)) for value in values)

def mean_impute(values: list[float | None]) -> list[float]:
    observed = [float(v) for v in values if v is not None and not (isinstance(v, float) and isnan(v))]
    if not observed:
        raise ValueError("cannot impute a column with no observed values")
    mean = sum(observed) / len(observed)
    return [mean if v is None or (isinstance(v, float) and isnan(v)) else float(v) for v in values]

if __name__ == "__main__":
    values = [2.0, None, 6.0, float("nan")]
    print("missing:", missing_count(values))
    print("imputed:", mean_impute(values))
