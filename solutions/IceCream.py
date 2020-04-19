'''
Schneider's Sweet Shop Ice Cream Blending Problem
'''

from pulp import *

INGREDIENTS = [f"X{i+1}" for i in range(14)]

COSTS = {key:value for key,value in zip(INGREDIENTS, [1.19, .7, 2.32, 2.3, 2.87, .25, .35, .65, .25, 1.75, 4.45, 2.45, 1.68, 0])}

FAT = {
    'X1': .4,
    'X2': .2,
    'X3': .8,
    'X4': .8,
    'X5': .9,
    'X6': .1,
    'X10': .5,
    'X11': .6
}

SERUM = {
    'X1': .1,
    'X4': .1,
    'X6': .1,
    'X7': .3,
    'X8': 1
}

WATER = {
    'X1': .5,
    'X2': .8,
    'X3': .2,
    'X4': .1,
    'X5': .1,
    'X6': .8,
    'X7': .7,
    'X9': .3,
    'X14': 1
}

prob = LpProblem("Schneider's Sweet Shop Ice Cream Blending Problem", LpMinimize)

ingr_vars = LpVariable.dicts("Ingredient", INGREDIENTS, 0)

# OBJ Function
prob += lpSum([COSTS[i] * ingr_vars[i] for i in INGREDIENTS]), "Total Cost of Batch"

# CONSTRAINTS - Desired Composition
""" prob += lpSum([FAT[i] * ingr_vars[i] for i in FAT]) == 16/2, "Fat Percentage"
prob += lpSum([SERUM[i] * ingr_vars[i] for i in SERUM]) == 8/2, "Serum Solids Percentage"
prob += lpSum([.7 * ingr_vars['X9'] + .1 * ingr_vars['X10']]) == 16/2, "Sugar Solids Percentage"
prob += lpSum([.4 * ingr_vars['X10'] + .4 * ingr_vars['X11']]) == .35/2, "Egg Solids Percentage"
prob += ingr_vars['X12'] == .25/2, "Stabilizer Percentage"
prob += ingr_vars['X13'] == .15/2, "Emulsifier Percentage"
prob += lpSum([WATER[i] * ingr_vars[i] for i in WATER]) == 59.25/2, "Water Percentage"
prob += lpSum([ingr_vars[i] for i in INGREDIENTS]) == 100/2, "Total of 50 lbs" """

# CONSTRAINTS - Relaxed Composition
prob += lpSum([FAT[i] * ingr_vars[i] for i in FAT]) >= 15/2, "Fat Low"
prob += lpSum([FAT[i] * ingr_vars[i] for i in FAT]) <= 17/2, "Fat High"
prob += lpSum([SERUM[i] * ingr_vars[i] for i in SERUM]) >= 7/2, "Serum Solids Low"
prob += lpSum([SERUM[i] * ingr_vars[i] for i in SERUM]) <= 9/2, "Serum Solids High"
prob += lpSum([.7 * ingr_vars['X9'] + .1 * ingr_vars['X10']]) >= 15.5/2, "Sugar Solids Low"
prob += lpSum([.7 * ingr_vars['X9'] + .1 * ingr_vars['X10']]) <= 16.5/2, "Sugar Solids High"
prob += lpSum([.4 * ingr_vars['X10'] + .4 * ingr_vars['X11']]) >= .3/2, "Egg Solids Low"
prob += lpSum([.4 * ingr_vars['X10'] + .4 * ingr_vars['X11']]) <= .4/2, "Egg Solids High"
prob += ingr_vars['X12'] >= .2/2, "Stabilizer Low"
prob += ingr_vars['X12'] <= .3/2, "Stabilizer High"
prob += ingr_vars['X13'] >= .1/2, "Emulsifier Low"
prob += ingr_vars['X13'] <= .2/2, "Emulsifier High"
prob += lpSum([WATER[i] * ingr_vars[i] for i in WATER]) >= 58/2, "Water Low"
prob += lpSum([WATER[i] * ingr_vars[i] for i in WATER]) <= 59.5/2, "Water High"
prob += lpSum([ingr_vars[i] for i in INGREDIENTS]) == 100/2, "Total of 50 lbs"

prob.writeLP("solutions/IceCream.lp")
prob.solve()
print(f"Status: {LpStatus[prob.status]}")


def get_ingr_name(ingredient):
    names = ['40% Cream', 'Sugared frozen fresh egg yolk', 'Powdered egg yolk', 'Stabilizer', 'Emulsifier', 'Water', 
    '23% Cream', 'Butter', 'Plastic cream', 'Butter oil', '4% Milk', 'Skim condensed milk', 'Skim milk powder', 'Liquid sugar']
    zipped = {name:var for name,var in zip([v.name for v in prob.variables()], names)}
    ingr_name = zipped[ingredient]
    return ingr_name

for v in prob.variables():
    print(f"{get_ingr_name(v.name)} = {round(v.varValue, 4)}")

print(f"Total Cost of Batch (Desired Composition): ${round(value(prob.objective), 2)}")

# Desired Composition = $25.35
# Relaxed Composition = $24.04
