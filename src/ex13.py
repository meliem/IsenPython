def compresser(chaine):

    nouvelle_chaine = ""
    count = 1

    for i in range(1, len(chaine)):
        if chaine[i] == chaine[i - 1]:
            count += 1
        else:
            nouvelle_chaine += chaine[i - 1] + str(count)
            count = 1

    nouvelle_chaine += chaine[-1] + str(count)

    return nouvelle_chaine

print(compresser("aaabbc"))
print(compresser("aabcccccaaa"))
print(compresser("abc"))
print(compresser("aaaa"))
