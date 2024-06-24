
from prettytable import PrettyTable
from scraper import scrape_ldlc

# les couleurs
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# Fonction pour scraper le site de ldlc pour obtenir le prix d'un produit
# Return une liste avec le nom du produit, le prix et si le produit est moins cher que le prix cher en couleur
def makeRow(query,prixCher):
    price=scrape_ldlc(query)
    if price>prixCher:
        return [query,price,f'{RED}No{RESET}']
    else:
        return [query,price,f'{GREEN}Yes{RESET}']
    
    
#Avec PrettyTable, on peut creer un tableau avec des colonnes
#pour chaque objet dans la liste objects, on cree une ligne avec makeRow
#On cree une nouvelle ligne avec makeRow
#On ajoute la ligne au tableau avec add_row
#On affiche le tableau avec print(table)
def makeTable(objects,prixCher):
    table = PrettyTable()
    table.field_names = ["Product", "Price", f"Moins cher que {prixCher}"]
    for query in objects:        #pour chaque objet dans la liste objects
        row=makeRow(query,prixCher) #on cree une ligne avec makeRow
        table.add_row(row)        #on ajoute la ligne au tableau avec add_row
    print(table)



if __name__ == '__main__':   #si on execute ce fichier directement
    #liste des objets a comparer
    objects=[
        'Ecran Acer 2027',
        'Ecran Samsung'
    ]
    #prix de reference
    prixCher=100

    makeTable(objects,prixCher)

