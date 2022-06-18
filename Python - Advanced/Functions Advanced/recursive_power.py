def recursive_power(n, pow):
    if pow == 0:
        return 1
    return n * recursive_power(n, pow - 1)