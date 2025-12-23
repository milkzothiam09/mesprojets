import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import pytz
from datetime import datetime


def info_numero_telephone(numero):
    """
    Donne des informations générales sur un numéro (pays, opérateur, fuseau horaire)
    ainsi que l'heure et la date actuelles du pays concerné.
    """
    try:
        # Parser le numéro
        num_parsed = phonenumbers.parse(numero, None)

        # Informations disponibles
        pays = geocoder.description_for_number(num_parsed, "fr")
        operateur = carrier.name_for_number(num_parsed, "fr")
        fuseaux = timezone.time_zones_for_number(num_parsed)

        print(f"Numéro: {phonenumbers.format_number(num_parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        print(f"Pays: {pays}")
        print(f"Opérateur: {operateur}")
        print(f"Fuseau(x) horaire(s): {', '.join(fuseaux)}")

        #Récupérer et afficher l'heure et la date 
        if fuseaux:  # Vérifier si un fuseau a été trouvé
            # Obtenir le fuseau horaire principal
            tz = pytz.timezone(fuseaux[0])
            # Obtenir la date et l'heure actuelles dans ce fuseau
            heure_actuelle = datetime.now(tz)
            # Formater l'affichage
            date_formatee = heure_actuelle.strftime("%A %d/%m/%Y")  # Ex: Mercredi 17/12/2025
            heure_formatee = heure_actuelle.strftime("%H:%M:%S")  # Ex: 10:39:37

            print(f"Date locale: {date_formatee}")
            print(f"Heure locale: {heure_formatee}")
        else:
            print("Fuseau horaire non spécifique, heure locale non disponible.")
        # ----------------------------------------------------------

    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Erreur de parsing du numéro: {e}")
    except Exception as e:
        print(f"Erreur inattendue: {e}")


# Exemple d'utilisation avec votre numéro
info_numero_telephone("+221773456789")