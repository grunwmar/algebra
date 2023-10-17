import math


def namingf(k, n, short=False):
    if short:
        names = ["s", f"v{k}", "i"]
    else:
        names = ["scalar", f"m{k}_vector", "pseudo_scalar"]
    if k == 0:
        return names[0]
    elif k == n:
        return names[2]
    else:
        return names[1]


def generate_basis_signature(n):
    base_classes = {}
    for k in range(0, n+1):
        c = math.comb(n, k)
        base_classes[k] = c

    return base_classes
