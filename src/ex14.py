def return_mail(chaine):
    tableau_de_mail = []
    for mot in chaine.split(" "):
        print(mot)
        for lettre in mot:
            if lettre == "@":
                tableau_de_mail.append(mot)
                break

    return tableau_de_mail

print(return_mail("Contactez-nous à support@email.com ou info@exemple.org"))

