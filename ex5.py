janvier = ["C01", "C02", "C03", "C05", "C08"]
fevrier = ["C02", "C03", "C04", "C08", "C09"]
mars    = ["C01", "C03", "C08", "C09", "C10"]

j, f, m = set(janvier), set(fevrier), set(mars)

# Clients venus les trois mois (intersection)
fideles = j & f & m
print("Les trois mois :", sorted(fideles))

# Clients venus au moins une fois (union)
tous = j | f | m
print("Au moins une fois :", sorted(tous))

# Nouveaux clients de mars (différence)
nouveaux = m - j - f
print("Nouveaux en mars :", sorted(nouveaux))