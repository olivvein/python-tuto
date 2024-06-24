# python-tuto
 
pour le tableau execute 

```sh
python comparateur.py 
```


pour tester le scrape :

```sh
python scraper.py
```





## explications du scope des variables :  ou déclarer une variable et ou est elle utilisable 



Notions de base sur le scoping

En Python, le “scope” (portée) d’une variable détermine où cette variable peut être accessible dans le code. Il y a principalement deux types de scopes:

	1.	Scope global: Les variables définies au niveau le plus haut du script, en dehors de toute fonction ou classe.
	2.	Scope local: Les variables définies à l’intérieur d’une fonction ou d’une classe, accessibles uniquement dans cette fonction ou classe.

Variables globales

Les variables globales sont définies au niveau du script, en dehors de toute fonction. Elles sont accessibles dans toutes les fonctions, à condition qu’on ne les redéfinisse pas à l’intérieur de ces fonctions.

Dans le code fourni, les variables globales sont:

	•	RED, GREEN, RESET: Ces variables contiennent des codes de couleur pour le texte et sont utilisées dans la fonction makeRow.
	•	prixCher: Utilisée pour comparer le prix des produits.
	•	objects: Contient la liste des produits à vérifier.
	•	Les fonctions makeRow et makeTable sont également définies au niveau global et peuvent être appelées depuis n’importe où dans le script.

Variables locales

Les variables locales sont définies à l’intérieur des fonctions et ne sont accessibles que dans le cadre de ces fonctions. Une fois que la fonction se termine, les variables locales ne sont plus accessibles.

Exemple de variables locales:

	1.	Dans la fonction makeRow:
	•	price: Est la variable locale qui stocke le prix du produit renvoyé par scrape_ldlc.
	•	query et prixCher: Bien qu’elles soient passées en tant que paramètres à la fonction, elles sont considérées comme des variables locales à cette fonction.
	2.	Dans la fonction makeTable:
	•	table: Est une variable locale qui crée un objet PrettyTable.
	•	query: Est une variable locale dans le contexte de la boucle for, représentant chaque produit de la liste objects.
	•	row: Est une variable locale qui stocke la ligne générée par makeRow.