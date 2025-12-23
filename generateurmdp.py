import secrets
import string

def generer_mot_de_passe(longueur=12):
    if longueur < 9:
        raise ValueError("La longueur doit être au moins de 4 caractères")

    # Jeux de caractères
    lettres = string.ascii_letters
    chiffres = string.digits
    symboles = string.punctuation

    # Garantir au moins un caractère de chaque type
    mot_de_passe = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(chiffres),
        secrets.choice(symboles)
    ]

    # Compléter le reste du mot de passe
    caracteres = lettres + chiffres + symboles
    mot_de_passe += [secrets.choice(caracteres) for _ in range(longueur - 4)]

    # Mélange sécurisé
    secrets.SystemRandom().shuffle(mot_de_passe)

    return ''.join(mot_de_passe)

# Exemple d'utilisation
print(generer_mot_de_passe(12))
