import copy

produit={
    "nom" : "aucun",
    "prix" : 0.0,
    "quantite" : 0
}

def getInputData():
    produitEnCours = copy.deepcopy(produit)
    produitEnCours["nom"] = input("Entrer le nom du produit: ")
    produitEnCours["prix"] = float(input("Entrer le prix du produit: "))
    produitEnCours["quantite"] = int(input("Entrer la quantite du produit: "))
    return produitEnCours

listeProduit = []
prixTotal = 0.0
nbreProduit = int(input("Combien de produit souhaitez-vous facturer? : "))
for i in range(0, nbreProduit):
    produitEnCours = getInputData()
    listeProduit.append(produitEnCours)
    prixTotal += produitEnCours["prix"] * produitEnCours["quantite"]    
    print(listeProduit)

    
print(f'Prix total = {prixTotal}')
