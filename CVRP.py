# cvrp_ortools.py
# Résout le CVRP (capacitated VRP) avec OR-Tools pour nos données d'exemple.
from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# Données
depot = (50.0, 50.0)
clients = [
    (52.0, 54.0, 400),   # id 1
    (48.0, 57.0, 250),   # id 2
    (55.0, 47.0, 300),   # id 3
    (45.0, 49.0, 150),   # id 4
    (53.5, 60.0, 600),   # id 5
    (46.0, 45.0, 200),   # id 6
]
capacity = 1000
num_vehicles = 5  # on alloue plus de véhicules que nécessaire ; OR-Tools n'utilisera que ceux nécessaires

# Construction des nœuds (0 = dépôt)
nodes = [depot] + [(c[0], c[1]) for c in clients]
demands = [0] + [c[2] for c in clients]

# Matrice des distances (float)
def euclid(a,b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

dist_matrix = [[euclid(nodes[i], nodes[j]) for j in range(len(nodes))] for i in range(len(nodes))]

# OR-Tools requires integer costs -> on scale
SCALE = 1000

# Manager & RoutingModel
manager = pywrapcp.RoutingIndexManager(len(dist_matrix), num_vehicles, 0)
routing = pywrapcp.RoutingModel(manager)

# Transit (distance) callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return int(dist_matrix[from_node][to_node] * SCALE)

trans_callback_idx = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(trans_callback_idx)

# Demand callback (capacity)
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return demands[from_node]

demand_callback_idx = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_idx,
    0,                    # null capacity slack
    [capacity] * num_vehicles,  # vehicle capacities
    True,                 # start cumul to zero
    'Capacity'
)

# Search parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
search_parameters.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
search_parameters.time_limit.seconds = 10

# Solve
solution = routing.SolveWithParameters(search_parameters)
if not solution:
    print("Aucune solution trouvée (vérifier l'installation OR-Tools / paramètres).")
    exit(1)

# Extract routes
total_distance = 0.0
used_vehicles = 0
for v in range(num_vehicles):
    index = routing.Start(v)
    if routing.IsEnd(solution.Value(routing.NextVar(index))):
        continue
    used_vehicles += 1
    route = []
    load = 0
    route_distance = 0.0
    while not routing.IsEnd(index):
        node = manager.IndexToNode(index)
        route.append(node)
        load += demands[node]
        next_index = solution.Value(routing.NextVar(index))
        if not routing.IsEnd(next_index):
            route_distance += dist_matrix[node][manager.IndexToNode(next_index)]
        else:
            # add last leg back to depot
            route_distance += dist_matrix[node][0]
        index = next_index
    # ensure depot at ends
    if route[0] != 0:
        route = [0] + route
    if route[-1] != 0:
        route = route + [0]
    print(f"Vehicle {v+1}: route = {' -> '.join(map(str, route))}, load = {load} L, distance ≈ {route_distance:.3f} km")
    total_distance += route_distance

print(f"\nTotal distance (all vehicles): {total_distance:.3f} km")
print(f"Vehicles used: {used_vehicles}")
