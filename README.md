# mesprojets 


#GENERATEUR MOT DE PASSE 

Ce programme Python sert à générer un mot de passe sécurisé de manière aléatoire. Il utilise des modules standards de Python conçus pour la sécurité et la manipulation de chaînes de caractères.
Le module secrets est utilisé pour produire des valeurs aléatoires fiables d’un point de vue cryptographique. Contrairement au module random, il est recommandé lorsqu’il s’agit de générer des mots de passe ou des informations sensibles. Le module string, quant à lui, fournit des ensembles de caractères prêts à l’emploi comme les lettres, les chiffres et les symboles.
La fonction generer_mot_de_passe prend en paramètre la longueur du mot de passe, avec une valeur par défaut de 12 caractères. Avant toute génération, le programme vérifie que la longueur demandée est suffisante. Si la longueur est inférieure au minimum requis, une exception est levée afin d’éviter la création de mots de passe trop faibles.
Ensuite, le programme définit différents jeux de caractères : les lettres (minuscules et majuscules), les chiffres et les caractères spéciaux. Pour garantir la robustesse du mot de passe, le script commence par sélectionner obligatoirement un caractère de chaque catégorie : une lettre minuscule, une lettre majuscule, un chiffre et un symbole. Cette étape assure que le mot de passe respecte les règles de complexité couramment utilisées en sécurité informatique.
Après cela, le reste du mot de passe est complété avec des caractères choisis aléatoirement parmi l’ensemble des lettres, chiffres et symboles, jusqu’à atteindre la longueur totale demandée. Chaque caractère est sélectionné à l’aide de secrets.choice, ce qui garantit un haut niveau d’imprévisibilité.
Une fois tous les caractères générés, ils sont mélangés de manière sécurisée afin d’éviter un ordre prévisible (par exemple, toujours commencer par une minuscule, puis une majuscule, etc.). Ce mélange renforce encore la sécurité du mot de passe.
Enfin, la liste de caractères est transformée en une chaîne de caractères unique qui représente le mot de passe final. Le programme retourne ce mot de passe, qui peut ensuite être affiché ou utilisé selon les besoins.



#GESTION DES TACHES

Ce programme est une application simple de gestion de tâches (to-do list) développée en Python et exécutée dans le terminal. Il permet à l’utilisateur de gérer une liste de tâches en offrant la possibilité de les afficher, d’en ajouter, d’en supprimer et de les sauvegarder dans un fichier texte afin qu’elles soient conservées entre deux exécutions du programme.

Le programme commence par définir plusieurs fonctions. La fonction show_tasks sert à afficher toutes les tâches présentes dans la liste. Elle parcourt la liste des tâches à l’aide de la fonction enumerate, ce qui permet d’afficher chaque tâche avec un numéro commençant à 1. Cela rend la sélection des tâches plus simple pour l’utilisateur. Un saut de ligne est ajouté avant et après l’affichage pour améliorer la lisibilité.

La fonction add_task permet à l’utilisateur d’ajouter une nouvelle tâche. Elle utilise la fonction input pour récupérer le texte saisi par l’utilisateur, puis ajoute cette tâche à la liste à l’aide de la méthode append. Un message de confirmation est ensuite affiché pour indiquer que la tâche a bien été ajoutée.

La fonction remove_task permet de supprimer une tâche existante. Elle commence par afficher la liste des tâches afin que l’utilisateur puisse voir les numéros correspondants. L’utilisateur entre ensuite le numéro de la tâche à supprimer. Ce numéro est converti en entier, puis diminué de 1, car les listes en Python commencent à l’index 0. Une vérification est effectuée pour s’assurer que le numéro est valide. Si c’est le cas, la tâche est supprimée avec la méthode pop et un message indique quelle tâche a été retirée. La structure try/except permet d’éviter les erreurs si l’utilisateur entre une valeur invalide ou non numérique.

La fonction save_tasks est responsable de la sauvegarde des tâches dans un fichier texte nommé tasks.txt. Elle ouvre le fichier en mode écriture et écrit chaque tâche sur une ligne différente. L’utilisation de with open garantit que le fichier est correctement fermé après l’écriture.

La fonction load_tasks permet de charger les tâches sauvegardées au démarrage du programme. Elle tente d’ouvrir le fichier tasks.txt en mode lecture et retourne une liste contenant toutes les lignes du fichier, après suppression des retours à la ligne. Si le fichier n’existe pas, une exception FileNotFoundError est levée et la fonction retourne simplement une liste vide, ce qui permet au programme de fonctionner normalement.

Après la définition des fonctions, la variable tasks est initialisée en appelant la fonction load_tasks, ce qui permet de récupérer automatiquement les tâches enregistrées lors d’une précédente utilisation.

Le programme principal fonctionne ensuite à l’aide d’une boucle infinie while True qui affiche un menu contenant quatre options : afficher les tâches, ajouter une tâche, supprimer une tâche ou sauvegarder et quitter. Le choix de l’utilisateur est récupéré via la fonction input, puis traité à l’aide de conditions if, elif et else. Chaque option appelle la fonction correspondante. Lorsque l’utilisateur choisit l’option de sauvegarde et de sortie, les tâches sont enregistrées dans le fichier et la boucle est interrompue grâce à l’instruction break, ce qui met fin au programme. Si l’utilisateur entre un choix invalide, un message d’erreur est affiché






#LOCALISATION AVEC NUMERO DE PHONE

Description du script
Ce script Python permet d’extraire des informations générales à partir d’un numéro de téléphone international. Il utilise la bibliothèque phonenumbers pour analyser le numéro et fournir des informations telles que le pays d’origine, l’opérateur téléphonique et le fuseau horaire associé. À partir du fuseau horaire, le script calcule ensuite la date et l’heure locales du pays correspondant au numéro.

Bibliothèques utilisées
Le script repose sur plusieurs bibliothèques :
phonenumbers : bibliothèque spécialisée dans l’analyse et la validation des numéros de téléphone internationaux. Elle permet d’identifier le pays, l’opérateur et le fuseau horaire.
pytz : permet de manipuler les fuseaux horaires et d’obtenir l’heure locale d’un pays donné.
datetime : utilisée pour récupérer et formater la date et l’heure actuelles.

Fonction principale
La fonction info_numero_telephone(numero) prend en paramètre un numéro de téléphone au format international (par exemple +221773456789) et affiche différentes informations le concernant.
Étapes de fonctionnement
Analyse du numéro
Le numéro fourni est d’abord analysé à l’aide de la fonction phonenumbers.parse. Cette étape transforme la chaîne de caractères en un objet exploitable par la bibliothèque.

Récupération des informations
Une fois le numéro analysé :
Le pays ou la région est obtenu grâce au module geocoder.
Le nom de l’opérateur téléphonique est récupéré via le module carrier.
Le ou les fuseaux horaires associés au numéro sont fournis par le module timezone.

Affichage des informations
Le script affiche :
Le numéro formaté au standard international
Le pays ou la région
L’opérateur téléphonique
Le ou les fuseaux horaires disponibles
Calcul de la date et de l’heure locales
Si au moins un fuseau horaire est trouvé, le script :
Sélectionne le premier fuseau horaire
Récupère la date et l’heure actuelles dans ce fuseau grâce à pytz et datetime
Formate la date et l’heure pour un affichage lisible
Si aucun fuseau horaire n’est disponible, un message indique que l’heure locale ne peut pas être déterminée.

Gestion des erreurs
Le script gère deux types d’erreurs :
Les erreurs de parsing lorsque le numéro est invalide ou mal formé
Les erreurs inattendues pour éviter que le programme ne s’arrête brutalement






#GENERER QRCODE

Ce programme est une application graphique écrite en Python qui permet de générer des QR Codes à partir d’un texte saisi par l’utilisateur. L’interface graphique est réalisée avec la bibliothèque Tkinter, et la génération des QR Codes est assurée par la bibliothèque externe qrcode.

Au début du programme, les bibliothèques Tkinter et qrcode sont importées. Tkinter permet de créer la fenêtre, les boutons, les champs de saisie et l’affichage des images, tandis que qrcode est utilisée pour créer les images de QR Code à partir d’une chaîne de caractères.

La fenêtre principale de l’application est ensuite créée à l’aide de la fonction Tk(). Son titre est défini comme « QR Code Generator », sa taille est fixée à 1000 pixels de largeur et 550 pixels de hauteur, et sa couleur de fond est configurée en rouge foncé. Le redimensionnement de la fenêtre est désactivé afin de conserver une interface stable. Une icône personnalisée est également ajoutée à la fenêtre à partir d’un fichier image nommé icon.png.

La fonction generer() est le cœur de l’application. Elle est exécutée lorsque l’utilisateur clique sur le bouton « Générer ». Cette fonction commence par récupérer le texte saisi dans le champ « Title », qui servira de nom de fichier pour le QR Code. Elle récupère ensuite le texte principal que l’utilisateur souhaite encoder. À partir de ce texte, un QR Code est généré grâce à la fonction qrcode.make(). L’image obtenue est ensuite sauvegardée au format PNG dans le dossier QRCODE, en utilisant le titre fourni par l’utilisateur comme nom de fichier.

Une fois le QR Code enregistré, l’image est rechargée dans l’application afin d’être affichée à l’écran. Une variable globale est utilisée pour stocker l’image, ce qui évite qu’elle soit supprimée par le système de gestion de mémoire de Tkinter. Le composant graphique prévu pour afficher l’image est alors mis à jour afin de montrer le QR Code généré.

L’interface graphique contient un label destiné à afficher le QR Code sur la partie droite de la fenêtre. Sur la partie gauche, un premier champ de saisie permet à l’utilisateur d’entrer le titre du QR Code, c’est-à-dire le nom du fichier. Un second champ de saisie est utilisé pour entrer le texte ou le lien à transformer en QR Code. Un bouton intitulé « Generer » permet de lancer la création du QR Code en appelant la fonction correspondante.

Enfin, la méthode mainloop() est appelée pour démarrer la boucle principale de Tkinter. Cette boucle permet à la fenêtre de rester ouverte, de répondre aux interactions de l’utilisateur et d’exécuter les actions associées aux boutons et aux champs de saisie
