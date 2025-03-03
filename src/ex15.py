def filtre(tableau, filtre):
    tableau_filtre = []
    for mot in tableau:
        if filtre in mot:
            tableau_filtre.append(mot)

    return tableau_filtre

print(filtre(["python", "java", "javascript", "c++"], "java"))

