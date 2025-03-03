phrase = "bonjour tout le monde"


def inverser_mots(phrase):
    mots = []
    mot_actuel = ""

    for char in phrase:
        if char == " ":
            if mot_actuel:
                mots.append(mot_actuel)
                mot_actuel = ""
        else:
            mot_actuel += char

    if mot_actuel:
        mots.append(mot_actuel)

    phrase_inverse = " ".join(mots[::-1])

    return phrase_inverse

print(inverser_mots("Bonjour tout le monde"))
