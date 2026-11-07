jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
ventes = [125000, 98000, 143500, 87000, 210000, 176500]

total = sum(ventes)
moyenne = total / len(ventes)

print(f"Total des ventes : {total}")
print(f"Moyenne journalière : {moyenne:.2f}")


print(f"Jour où les ventes ont été les plus fortes : {jours[ventes.index(max(ventes))]}")

print("Jours dont les ventes dépassent la moyenne :")
for jour, vente in zip(jours, ventes):
    if vente > moyenne:
        print(f"- {jour} : {vente}")

classement = sorted(zip(jours, ventes), key=lambda element: element[1], reverse=True)
print("Classement des jours, de la meilleure à la plus faible vente :")
for rang, (jour, vente) in enumerate(classement, start=1):
    print(f"{rang}. {jour} : {vente}")