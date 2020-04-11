'''
Foster Generators Transportation Problem
--- Practice Problem ---
'''

from pulp import *

# Origin nodes (Plants)
PLANTS = ['Cleveland', 'Bedford', 'York']
SUPPLY = {
    'Cleveland': 5000,
    'Bedford': 6000,
    'York': 2500
}

# Destination nodes (Distribution Centers)
DIST_CENTERS = ['Boston', 'Chicago', 'St. Louis', 'Lexington']
DEMAND = {
    'Boston': 6000,
    'Chicago': 4000,
    'St. Louis': 2000,
    'Lexington': 1500
}

# Transportation costs
COSTS = [
    [3, 2, 7, 6],   # Cleveland
    [7, 5, 2, 3],   # Bedford
    [2, 5, 4, 5]    # York
]
COSTS = makeDict([PLANTS, DIST_CENTERS], COSTS, 0)

# create problem and routes 
prob = LpProblem("Foster_Generators_Practice_Transportation_Problem", LpMinimize)
ROUTES = [(p, d) for p in PLANTS for d in DIST_CENTERS]
route_vars = LpVariable.dicts("Route", (PLANTS, DIST_CENTERS), 0, None, LpInteger)

# Add obj. function to problem
prob += lpSum([route_vars[p][d] * COSTS[p][d] for (p, d) in ROUTES]), "Sum of Transporting Costs"

# Add supply/demand constraints
for p in PLANTS:
    prob += lpSum([route_vars[p][d] for d in DIST_CENTERS]) <= SUPPLY[p], "Sum of Shipment From %s" %p

for d in DIST_CENTERS:
    prob += lpSum([route_vars[p][d] for p in PLANTS]) == DEMAND[d], "Sum of Shipment into %s" %d

# Solve problem
prob.writeLP("FosterGenTransportation.lp")
prob.solve()
print("Status: ", LpStatus[prob.status])

# print results
for v in prob.variables():
    print(f"{v.name} = {v.varValue}")
print(f"Optimal Objective Value: ${value(prob.objective)}")