from itertools import permutations, combinations

# --- Données ---
clients = [1,2,3,4,5]
demands = {1:2,2:3,3:2,4:3,5:1}
Q = 5

# Matrice des distances (symétrique)
d = {
    (0,1):4,(1,0):4,
    (0,2):6,(2,0):6,
    (0,3):5,(3,0):5,
    (0,4):7,(4,0):7,
    (0,5):3,(5,0):3,
    (1,2):3,(2,1):3,
    (1,3):4,(3,1):4,
    (1,4):6,(4,1):6,
    (1,5):2,(5,1):2,
    (2,3):2,(3,2):2,
    (2,4):4,(4,2):4,
    (2,5):5,(5,2):5,
    (3,4):3,(4,3):3,
    (3,5):4,(5,3):4,
    (4,5):6,(5,4):6
}

# --- Fonction pour calculer le coût d'une tournée ---
def route_cost(seq):
    if not seq: return 0
    cost = d[(0, seq[0])]  # départ dépôt → premier client
    for i in range(len(seq)-1):
        cost += d[(seq[i], seq[i+1])]  # client → client
    cost += d[(seq[-1], 0)]  # dernier client → dépôt
    return cost

# --- Fonction pour trouver le meilleur ordre TSP pour un sous-ensemble ---
def best_tsp(subset):
    best_cost = float('inf')
    best_perm = None
    for perm in permutations(subset):
        c = route_cost(perm)
        if c < best_cost:
            best_cost = c
            best_perm = perm
    return best_cost, best_perm

# --- Méthode combinatoire ---
def combinatorial_vrp(clients, demands, Q):
    from itertools import chain
    # Fonction récursive pour générer toutes les partitions
    def partitions(lst):
        if not lst: yield []
        else:
            first = lst[0]
            for part in partitions(lst[1:]):
                yield [[first]] + [p[:] for p in part]
                for i in range(len(part)):
                    new_part = [p[:] for p in part]
                    new_part[i] = new_part[i] + [first]
                    yield new_part

    # Eviter les doublons
    seen = set()
    best_solution = None
    best_total_cost = float('inf')

    for p in partitions(clients):
        norm = tuple(sorted(tuple(sorted(sub)) for sub in p))
        if norm in seen: continue
        seen.add(norm)
        feasible = True
        total_cost = 0
        routes_info = []
        for subset in norm:
            demand = sum(demands[c] for c in subset)
            if demand > Q:
                feasible = False
                break
            cost, order = best_tsp(subset)
            total_cost += cost
            routes_info.append((subset, order, cost))
        if feasible and total_cost < best_total_cost:
            best_total_cost = total_cost
            best_solution = routes_info

    return best_solution, best_total_cost

# --- Méthode Clarke & Wright ---
def clarke_wright_vrp(clients, demands, Q, d):
    # Initialiser une tournée par client
    routes = {c:[c] for c in clients}

    # Calcul des savings
    savings = []
    for i in clients:
        for j in clients:
            if i<j:
                s = d[(0,i)] + d[(0,j)] - d[(i,j)]
                savings.append((s,i,j))
    savings.sort(reverse=True)  # tri décroissant

    for s,i,j in savings:
        # Trouver les routes contenant i et j
        route_i = next((r for r in routes.values() if i in r), None)
        route_j = next((r for r in routes.values() if j in r), None)
        if route_i == route_j: continue  # même route
        # Vérifier capacité
        demand_i = sum(demands[c] for c in route_i)
        demand_j = sum(demands[c] for c in route_j)
        if demand_i + demand_j <= Q:
            # Fusionner : i en fin de route_i, j en début de route_j (ou inverse)
            new_route = route_i + route_j
            # Supprimer anciennes routes
            for key in list(routes.keys()):
                if key in route_i or key in route_j:
                    del routes[key]
            # Ajouter nouvelle route
            routes[new_route[0]] = new_route

    # Calcul du coût total
    total_cost = 0
    final_routes = []
    for r in routes.values():
        c = route_cost(r)
        final_routes.append((r, c))
        total_cost += c

    return final_routes, total_cost

# --- Exécution ---
comb_solution, comb_cost = combinatorial_vrp(clients, demands, Q)
cw_solution, cw_cost = clarke_wright_vrp(clients, demands, Q, d)

# --- Affichage ---
print("=== Solution combinatoire optimale ===")
for r in comb_solution:
    print(f"Tournée {r[0]} -> ordre optimal {r[1]} -> coût {r[2]}")
print(f"Coût total = {comb_cost}\n")

print("=== Solution Clarke & Wright ===")
for r in cw_solution:
    print(f"Tournée {r[0]} -> coût {r[1]}")
print(f"Coût total = {cw_cost}")
