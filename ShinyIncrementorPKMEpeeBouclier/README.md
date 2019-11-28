# This is the shiny incrementor for Pokemon Sword&Shield for Twitch streamers !

### REQUIREMENTS :

	- Python 3.6
	- Librairies python nécessaires : win32gui, pytesseract, PIL (pour installer les librairies python il faut utiliser pip)
	  Exemple : pip install win32gui
		    pip install pytesseract
		    pip install PIL
	- Télécharger Tesseract-OCR -> https://github.com/UB-Mannheim/tesseract/wiki
	- Ajouter le path du dossier Tesseract-OCR aux variables d'environnements (regarder sur google comment ajouter un path au variable d'environnement)
	  Exemple de path : C:\Program Files\Tesseract-OCR



### INSTALLATION STEP BY STEP FOR NOOBS :

1) Install last version of Python3
2) Open a command prompt and do these lines :
	- pip install win32gui
	- pip install pytesseract
	- pip install PIL
3) Donwload Tesseract-OCR -> https://github.com/UB-Mannheim/tesseract/wiki
4) Add the path of Tesseract-OCR into your paths variable (tutorial for windows : https://docs.alfresco.com/4.2/tasks/fot-addpath.html)



### UTILISATION (version 1.0) :

	- Pour lancer le programme python :
		- Ouvrir une invite de commande.
		- Aller dans le dossier du fichier python (ex: C:\Users\toi\ShinyIncrementorPKMEpeeBouclier)
		- Lancer la commande : python lainkapete.py
		- Ecrire le nom du pokémon recherché en question (avec Majuscule au début !).
		- Laisser tourner :D
	- Pour fermer le programme Ctrl+C dans l'invite de commande lol
	- L'incrémentation est stocké dans le fichier texte "number.txt" qui indique le nombre d'incrémentation. Tu peux le reset en écrivant 0 dedans et sauvegarder.
	  C'est aussi ici que tu pourras récupérer le nombre et l'afficher sur ton stream.
	- ATTENTION : Si vous avez un overlay réduisant la taille du retour de Pokémon, il faut changer la ligne 57 du code pour que vous puissiez capturer exactement le nom du pokémon.
