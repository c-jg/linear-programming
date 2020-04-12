'''
TJ Inc.'s Product Mix Blending Problem
'''
from pulp import *

# Variables
MIXES = ['REGULAR', 'DELUXE', 'HOLIDAY']

PROFIT = {
    'REGULAR': 1.65,
    'DELUXE': 2,
    'HOLIDAY': 2.25
}

DEMAND = {
    'REGULAR': 10000,
    'DELUXE': 3000,
    'HOLIDAY': 5000
}

ALMOND_PERCENT = {
    'REGULAR': .15,
    'DELUXE': .2,
    'HOLIDAY': .25
}

BRAZIL_PERCENT = {
    'REGULAR': .25,
    'DELUXE': .2,
    'HOLIDAY': .15
}

FILBERT_PERCENT = {
    'REGULAR': .25,
    'DELUXE': .2,
    'HOLIDAY': .15
}

PECAN_PERCENT = {
    'REGULAR': .1,
    'DELUXE': .2,
    'HOLIDAY': .25
}

WALNUT_PERCENT = {
    'REGULAR': .25,
    'DELUXE': .2,
    'HOLIDAY': .2
}

# Create problem
prob = LpProblem("TJ Nut Mixes Blending Problem", LpMaximize)

mix_vars = LpVariable.dicts("Mix", MIXES, 0)

# Add obj. function to problem
prob += lpSum([mix_vars[i] * PROFIT[i] for i in MIXES]) - 36450, "Total Profit Contribution"

# Set constraints
prob += lpSum([ALMOND_PERCENT[i] * mix_vars[i] for i in MIXES]) <= 6000, "Almond Amount"
prob += lpSum([BRAZIL_PERCENT[i] * mix_vars[i] for i in MIXES]) <= 7500, "Brazil Amount"
prob += lpSum([FILBERT_PERCENT[i] * mix_vars[i] for i in MIXES]) <= 7500, "Filbert Amount"
prob += lpSum([PECAN_PERCENT[i] * mix_vars[i] for i in MIXES]) <= 6000, "Pecan Amount"
prob += lpSum([WALNUT_PERCENT[i] * mix_vars[i] for i in MIXES]) <= 7500, "Walnut Amount"
prob += mix_vars['REGULAR'] >= 10000, "Regular Amount"
prob += mix_vars['DELUXE'] >= 3000, "Deluxe Amount"
prob += mix_vars['HOLIDAY'] >= 5000, "Holiday Amount"

prob.writeLP("TJMixes.lp")
prob.solve()
print(f"Status: {LpStatus[prob.status]}")

for v in prob.variables():
    print(f"{v.name} = {v.varValue}")

print(f"Total profit: ${value(prob.objective)}")