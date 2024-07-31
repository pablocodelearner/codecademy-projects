import numpy as np

def calculate(l):
    if len(l) != 9:
        raise ValueError("List must contain nine numbers.")
    a = np.array(l)
    x = a.reshape(3, 3)
    x_mean = [list(x.mean(axis=0)), list(x.mean(axis=1)), x.mean()]
    x_var = [list(x.var(axis=0)), list(x.var(axis=1)), x.var()]
    x_std = [list(x.std(axis=0)), list(x.std(axis=1)), x.std()]
    x_max = [list(x.max(axis=0)), list(x.max(axis=1)), x.max()]
    x_min = [list(x.min(axis=0)), list(x.min(axis=1)), x.min()]
    x_sum = [list(x.sum(axis=0)), list(x.sum(axis=1)), x.sum()]
    calculations = {
        'mean': x_mean,
        'variance': x_var,
        'standard deviation': x_std,
        'max': x_max,
        'min': x_min,
        'sum': x_sum
    }
    return calculations