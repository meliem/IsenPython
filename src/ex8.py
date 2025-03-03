def calcul_serie(n):
    return sum(1 / (2 ** k) for k in range(n + 1))


def affichage_valeurs_serie(N):
    for n in range(N + 1):
        print(f"S({n}) = {calcul_serie(n)}")
