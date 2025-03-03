def somme_cible(tableau, cible):
    tableau_de_retour = []
    for i in range(len(tableau)):
        for j in range(i + 1, len(tableau)):
            if tableau[i] + tableau[j] == cible:
                tableau_de_retour.append([tableau[i], tableau[j]])

    return tableau_de_retour

print(somme_cible([1, 2, 3, 4, 5, 6], 7))