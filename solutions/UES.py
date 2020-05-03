'''
United Express Service (UES) Assignment Problem
'''

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Bid prices
bids = {
    'MP': [190, 175, 125, 230],
    'SM': [150, 235, 155, 220],
    'MC': [210, 225, 135, 260],
    'DB': [170, 185, 190, 280],
    'LF': [220, 190, 140, 240],
    'LD': [270, 200, 130, 260]
}

# Create nodes - VISUAL ONLY
a = ['LD', 'LF', 'DB', 'MC', 'SM', 'MP']
b = [4, 3, 2, 1]
G.add_nodes_from([*a,*b])

# Position nodes
l,r = 1,2
for i in G.nodes:
    if l <= len(a):
        G.nodes[i]['pos'] = (1,l)
        G.nodes[i]['supply'] = 1
        l += 1
    else:
        G.nodes[i]['pos'] = (5,r)
        G.nodes[i]['demand'] = 1
        r += 1

# Draw routes
G.add_edges_from([(origin,dest) for origin in a for dest in b])

# Position supply/demand
pos = nx.get_node_attributes(G, "pos")
sup = nx.get_node_attributes(G, 'supply')
dem = nx.get_node_attributes(G, 'demand')

dem_loc, sup_loc = {}, {}
for x in pos:
    if x in a:
        sup_loc[x] = (pos[x][0]-.15, pos[x][1])
    else:
        dem_loc[x] = (pos[x][0]+.15, pos[x][1])

# Add bid price to edges
for i in G.edges:
    G.edges[i]['bid'] = bids[i[0]][i[1]-1]

bid_prices = nx.get_edge_attributes(G, 'bid')

# Display network
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_labels(G, sup_loc, labels=sup)
nx.draw_networkx_labels(G, dem_loc, labels=dem)
nx.draw_networkx_edge_labels(G, pos, bid_prices, font_size=6, label_pos=.82)
plt.show()

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

# Formulate LP problem

from pulp import *

ORIGINS = ['MP', 'SM', 'MC', 'DB', 'LF', 'LD']
DESTINATIONS = [1, 2, 3, 4]
# Supply/demand = 1 for all

PRICES = [
    [190, 175, 125, 230], 
    [150, 235, 155, 220], 
    [210, 225, 135, 260], 
    [170, 185, 190, 280], 
    [220, 190, 140, 240], 
    [270, 200, 130, 260]
]

PRICES = makeDict([ORIGINS, DESTINATIONS], PRICES, 0)

prob = LpProblem("UES_Assignment_Problem", LpMinimize)

ROUTES = [(o,d) for o in ORIGINS for d in DESTINATIONS]
route_vars = LpVariable.dicts("Routes", (ORIGINS,DESTINATIONS), 0, None, LpInteger)

prob += lpSum([route_vars[o][d] * PRICES[o][d] for (o,d) in ROUTES]), "Total Cost"

for o in ORIGINS:
    prob += lpSum([route_vars[o][d] for d in DESTINATIONS]) <= 1, f"Supply Constraint for {o}"

for d in DESTINATIONS:
    prob += lpSum([route_vars[o][d] for o in ORIGINS]) == 1, f"Demand Constraint for {d}"

prob.writeLP('solutions/UES.lp')
prob.solve()
print(f"Status: {LpStatus[prob.status]}")

for v in prob.variables():
    if v.varValue == 1:
        cost = PRICES[v.name.split('_')[1]][int(v.name[-1])]
        print(f"{v.name.split('_')[1]} (${cost}) ---> {v.name[-1]}")

print(f"Total cost: ${round(value(prob.objective))}")
    