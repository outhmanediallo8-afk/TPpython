catalogue = {
    "P01": {"nom": "Ordinateur portable", "categorie": "Informatique", "prix": 45000},
    "P02": {"nom": "Imprimante", "categorie": "Informatique", "prix": 12000},
    "P03": {"nom": "Chaise de bureau", "categorie": "Mobilier", "prix": 6500},
    "P04": {"nom": "Ramette papier", "categorie": "Fournitures", "prix": 350},
}

# a) Ajouter le produit P05
catalogue["P05"] = {"nom": "Bureau", "categorie": "Mobilier", "prix": 18000}

# b) Augmenter de 5 % (arrondi à l'unité) le prix des produits Informatique
for ref, produit in catalogue.items():
    if produit["categorie"] == "Informatique":
        produit["prix"] = round(produit["prix"] * 1.05)

# c) Supprimer le produit P04
del catalogue["P04"]          # ou : catalogue.pop("P04")

# d) Afficher le catalogue sous forme de tableau aligné
def afficher_catalogue(cat):
    print(f"{'Réf':<6}{'Nom':<22}{'Catégorie':<15}{'Prix (MRU)':>12}")
    print("-" * 55)
    for ref, p in cat.items():
        print(f"{ref:<6}{p['nom']:<22}{p['categorie']:<15}{p['prix']:>12,}".replace(",", " "))

afficher_catalogue(catalogue)

# e) Prix moyen par catégorie
totaux = {}
for p in catalogue.values():
    cat = p["categorie"]
    if cat not in totaux:
        totaux[cat] = [0, 0]          # [somme des prix, nombre de produits]
    totaux[cat][0] += p["prix"]
    totaux[cat][1] += 1

print("\nPrix moyen par catégorie :")
for cat, (somme, n) in totaux.items():
    print(f"{cat:<15}{somme / n:>12.2f} MRU")