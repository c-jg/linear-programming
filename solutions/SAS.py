'''
Sports of All Sorts Transshipment Problem
pg. 302 #13
'''

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# nodes 
factories = {'DT':350,'LA':350,'AS':700}
dcs = {'IA':500,'MY':500,'ID':500,'AK':500}
retailers = {'JSS':200,'SNS':500,'TSD':650}

G.add_nodes_from([*list(factories.keys())[::-1], *list(dcs.keys())[::-1], *list(retailers.keys())[::-1]])

x = 1
for i in G.nodes:
    if x < 4:
        G.nodes[i]['pos'] = (1,x)
        G.nodes[i]['sup'] = factories[i]
        x += 1
    elif x < 8:
        G.nodes[i]['pos'] = (2,x-3.5)
        G.nodes[i]['cap'] = dcs[i]
        x += 1
    else:
        G.nodes[i]['pos'] = (3,x-7)
        G.nodes[i]['dem'] = retailers[i]
        x += 1

G.add_edges_from([(f,d) for f in factories for d in dcs])
G.add_edges_from([(d,r) for d in dcs for r in retailers])

# Add costs to edges
costs = [40,40,42.5,32.5,35,45,35,42.5,25,25,35,40,27.5,25,42.5,35,40,32.5,20,32.5,40,30,27.5,30]

c = 0
for i in G.edges:
    G.edges[i]['cost'] = costs[c]
    c += 1

pos = nx.get_node_attributes(G, 'pos')
sup = nx.get_node_attributes(G, 'sup')
dem = nx.get_node_attributes(G, 'dem')
cap = nx.get_node_attributes(G, 'cap')
cost = nx.get_edge_attributes(G, 'cost')


dem_loc, sup_loc, cap_loc = {}, {}, {}
for x in pos:
    if x in factories.keys():
        sup_loc[x] = (pos[x][0], pos[x][1]+.15)
    elif x in retailers.keys():
        dem_loc[x] = (pos[x][0], pos[x][1]+.15)
    else:
        if x == 'IA':
            cap_loc[x] = (pos[x][0], pos[x][1]-.15)
        else:
            cap_loc[x] = (pos[x][0], pos[x][1]+.15)

nx.draw_networkx_labels(G, dem_loc, labels=dem, font_size=8.5)
nx.draw_networkx_labels(G, sup_loc, labels=sup, font_size=8.5)
nx.draw_networkx_labels(G, cap_loc, labels=cap, font_size=8.5)
nx.draw_networkx_edge_labels(G, pos, cost, font_size=6, label_pos=.825)

nx.draw(G, pos, with_labels=True, font_size=8.5)
plt.tight_layout()
plt.show()

# ------------------------------------------------------
# SOLVE LP PROBLEM
# ------------------------------------------------------


from pulp import *

# Routes and costs 
ROUTES = {
    ('DT', 'IA'): 25, ('DT', 'MY'): 25, ('DT', 'ID'): 35, ('DT', 'AK'): 40, 
    ('LA', 'IA'): 35, ('LA', 'MY'): 45, ('LA', 'ID'): 35, ('LA', 'AK'): 42.5, 
    ('AS', 'IA'): 40, ('AS', 'MY'): 40, ('AS', 'ID'): 42.5, ('AS', 'AK'): 32.5, 
    ('IA', 'JSS'): 30, ('IA', 'SNS'): 27.5, ('IA', 'TSD'): 30,
    ('MY', 'JSS'): 20, ('MY', 'SNS'): 32.5, ('MY', 'TSD'): 40,
    ('ID', 'JSS'): 35, ('ID', 'SNS'): 40, ('ID', 'TSD'): 32.5, 
    ('AK', 'JSS'): 27.5, ('AK', 'SNS'): 25, ('AK', 'TSD'): 42.5
}

# Group supply/capacity/demand values
NODES = [*factories.keys(), *dcs.keys(), *retailers.keys()]
NODE_DATA = {}
for node in NODES:
    for i in list(ROUTES.keys()):
        if node in i[0]:
            try:
                NODE_DATA[f"{node}_O"].append(i)
            except:
                NODE_DATA[f"{node}_O"] = [i]
        if node in i[1]:
            try:
                NODE_DATA[f"{node}_I"].append(i)
            except:
                NODE_DATA[f"{node}_I"] = [i]

# problem
prob = LpProblem("Sports_of_All_Sorts_Transshipment", LpMinimize)
route_vars = LpVariable.dicts("Route", ROUTES, 0, None, LpInteger)

# Objective function
prob += lpSum([route_vars[x] * ROUTES[x] for x in ROUTES]), "Sum of Shipping Costs"

# Supply Constraints
for f in factories:
    prob += lpSum([route_vars[f] for f in NODE_DATA[f"{f}_O"]]) <= factories[f], f"Sum of Shipment from {f}"

# Capacity Constraints
for d in dcs:
    prob += lpSum([route_vars[x] for x in NODE_DATA[f"{d}_I"]]) <= 500, f"Sum of Shipments to {d}"
    prob += lpSum([route_vars[x] for x in NODE_DATA[f"{d}_I"]]) - lpSum([route_vars[x] for x in NODE_DATA[f"{d}_O"]]) == 0, f"Equal Shipments in/out of {d}"

# Demand Constraints
for f in retailers:
    prob += lpSum([route_vars[f] for f in NODE_DATA[f"{f}_I"]]) == retailers[f], f"Sum of shipments to {f}"

# Solve problem
prob.writeLP("solutions/SAS.lp")
prob.solve()
print(f"Status: {LpStatus[prob.status]}")

# Print results
for v in prob.variables():
    print(f"{v.name} = {int(v.varValue)}")
print(f"Optimal Objective Value: ${round(value(prob.objective),2)}")
