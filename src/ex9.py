def est_parfait(n):
    return n == sum(i for i in range(1, n) if n % i == 0)
