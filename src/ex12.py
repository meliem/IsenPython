def palyndrome(mot):
    inverse = ""
    for i in range(len(mot)-1, -1, -1):
        inverse += mot[i]
    return mot == inverse

print(palyndrome("radar"))
