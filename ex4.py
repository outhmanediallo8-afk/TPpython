ventes = [("Aicha", 12000), ("Sidi", 8000), ("Aicha", 15500),
          ("Mohamed", 4000), ("Sidi", 22000), ("Aicha", 3000),
          ("Fatimetou", 18000)]

# a) Nombre de vendeurs distincts avec un ensemble
vendeurs = {nom for nom, montant in ventes}
print("Vendeurs distincts :", len(vendeurs))

# b) Nombre de ventes et chiffre d'affaires par vendeur
nb_ventes = {}
chiffre_affaires = {}

for nom, montant in ventes:
    nb_ventes[nom] = nb_ventes.get(nom, 0) + 1
    chiffre_affaires[nom] = chiffre_affaires.get(nom, 0) + montant

print("Nombre de ventes :", nb_ventes)
print("Chiffre d'affaires :", chiffre_affaires)

# c) Vendeurs par chiffre d'affaires décroissant
classement = sorted(chiffre_affaires.items(), key=lambda x: x[1], reverse=True)

print(f"\n{'Vendeur':<12}{'CA (MRU)':>12}")
print("-" * 24)
for nom, ca in classement:
    print(f"{nom:<12}{ca:>12,}".replace(",", " "))