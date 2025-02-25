def get_average(liste):
    j = 0
    for i in liste:
        j += i
    return j/len(liste)

def get_weighted_average(pondered_list):
    j = 0
    k = 0
    for i in pondered_list:
        j += i[0] * i[1]
        k += i[1]

    return j / len(pondered_list) / k





