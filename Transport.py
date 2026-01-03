import pulp

# Données
supply = [100, 150]             # Offre des sources S1 et S2
demand = [80, 120, 50]          # Demande des destinations D1, D2, D3
costs = [[2, 3, 1],             # Coûts unitaires
         [5, 4, 8]]

sources = ["S1", "S2"]
destinations = ["D1", "D2", "D3"]

# Création du problème (Minimisation)
prob = pulp.LpProblem("Transport_Minimisation", pulp.LpMinimize)

# Variables de décision X[i,j] >= 0
x = pulp.LpVariable.dicts("X",
                          ((i, j) for i in range(len(sources)) for j in range(len(destinations))),
                          lowBound=0,
                          cat='Continuous')

# Fonction objectif : min Z = sum(Cij * Xij)
prob += pulp.lpSum(costs[i][j] * x[i, j] for i in range(len(sources)) for j in range(len(destinations)))

# Contraintes d'offre
for i in range(len(sources)):
    prob += pulp.lpSum(x[i, j] for j in range(len(destinations))) <= supply[i]

# Contraintes de demande
for j in range(len(destinations)):
    prob += pulp.lpSum(x[i, j] for i in range(len(sources))) == demand[j]

# Résolution
prob.solve()

# Affichage des résultats
print("Status:", pulp.LpStatus[prob.status])
print("Solution optimale :")
for i in range(len(sources)):
    for j in range(len(destinations)):
        print(f"X[{sources[i]},{destinations[j]}] =", x[i,j].varValue)

print("Coût total minimal Z =", pulp.value(prob.objective))
