def get_dividers(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def get_string(n):
    dividers = get_dividers(n)
    count = len(dividers)
    div_str = " ".join(map(str, dividers))

    return f"Le nombre {n} possède {count} diviseur(s) qui est/sont le(s) suivant(s) : {div_str}"

print(get_string(95))
print(get_dividers(95))