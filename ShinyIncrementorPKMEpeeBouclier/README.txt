#####CREATED BY VICOTEEN#####

This is the shiny incrementor of Pokemon Sword&Shield for Twitch streamers !

STEP BY STEP FOR NOOBS :

1) Install last version of Python3
2) Open a command prompt and do these lines :
	- pip install win32gui
	- pip install pytesseract
	- pip install PIL
3) Donwload Tesseract-OCR -> https://github.com/UB-Mannheim/tesseract/wiki
4) Add the path of Tesseract-OCR into your paths variable (tutorial for windows : https://docs.alfresco.com/4.2/tasks/fot-addpath.html)
5) Open a NEW command prompt and go to the folder where the file lainkapete.py is (use command cd to change folder)
6) Type the command : python lainkapete.py
7) Type the name of your Pokemon with the first letter in caps (ex: Stalgamin)













#####PREVIOUS EXPLANATION#####

PRE-REQUIS :
	
	- Python 3.6
	- Librairies python n�cessaires : win32gui, pytesseract, PIL (pour installer les librairies python il faut utiliser pip)
	  Exemple : pip install win32gui
		    pip install pytesseract
		    pip install PIL
	- T�l�charger Tesseract-OCR -> https://github.com/UB-Mannheim/tesseract/wiki
	- Ajouter le path du dossier Tesseract-OCR aux variables d'environnements (regarder sur google comment ajouter un path au variable d'environnement)
	  Exemple de path : C:\Program Files\Tesseract-OCR

UTILISATION :
	
	- Pour lancer le programme python :
		- Ouvrir une invite de commande.
		- Aller dans le dossier du fichier python (ex: C:\Users\toi\ShinyIncrementorPKMEpeeBouclier)
		- Lancer la commande : python lainkapete.py
		- Ecrire le nom du pok�mon recherch� en question (avec Majuscule au d�but !).
		- Laisser tourner :D
	- Pour fermer le programme Ctrl+C dans l'invite de commande lol
	- L'incr�mentation est stock� dans le fichier texte "number.txt" qui indique le nombre d'incr�mentation. Tu peux le reset en �crivant 0 dedans et sauvegarder.
	  C'est aussi ici que tu pourras r�cup�rer le nombre et l'afficher sur ton stream.

ATTENTION : Si vous avez un overlay r�duisant la taille du retour de Pok�mon, il faut changer la ligne 57 du code pour que vous puissiez capturer exactement le nom du pok�mon.
