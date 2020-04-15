'''
Flamingo Grill - Haskell & Johnson Advertising Campaign Problem
'''

from pulp import *

# MEDIA FORMS: TV(T), RADIO(R), ONLINE(N)
# 1: RELIABLE
# 2: DECLINE
MEDIUMS = ['T1', 'T2', 'R1', 'R2', 'N1', 'N2']

EXPOSURE_RATING = {
    'T1': 90,
    'T2': 55,
    'R1': 25,
    'R2': 20,
    'N1': 10,
    'N2': 5
}

CUSTOMERS_PER_AD = {
    'T1': 4000,
    'T2': 1500,
    'R1': 2000,
    'R2': 1200,
    'N1': 1000,
    'N2': 800
}

COST_PER_AD = {
    'T1': 10000,
    'T2': 10000,
    'R1': 3000,
    'R2': 3000,
    'N1': 1000,
    'N2': 1000
}

prob = LpProblem("Advertising Campaign Problem", LpMaximize)

medium_vars = LpVariable.dicts("Media", MEDIUMS, 0)

# OBJ. FUNCTION
prob += lpSum([medium_vars[m] * EXPOSURE_RATING[m] for m in MEDIUMS]), "Total Exposure Rating"

# CONSTRAINTS
prob += lpSum([COST_PER_AD[a] * medium_vars[a] for a in MEDIUMS]) <= 279000, "Total Budget"
prob += lpSum([CUSTOMERS_PER_AD[a] * medium_vars[a] for a in MEDIUMS]) >= 100000, "Total New Customers"
prob += medium_vars['T1'] <= 10, "Reliable TV" 
prob += medium_vars['R1'] <= 15, "Reliable Radio"
prob += medium_vars['N1'] <= 20, "Reliable Online"
prob += 2 * medium_vars['T1'] + 2 * medium_vars['T2'] - medium_vars['R1'] - medium_vars['R2'] <= 0, "Twice As Many Radio Ads As TV"
prob += medium_vars['T1'] + medium_vars['T2'] <= 20, "No More Than 20 TV Ads"
prob += 10000 * medium_vars['T1'] + 10000 * medium_vars['T2'] >= 140000, "TV Budget At Least $140,000"
prob += 3000 * medium_vars['R1'] + 3000 * medium_vars['R2'] <= 99000, "Radio Budget Max: $99,000"
prob += 1000 * medium_vars['N1'] + 1000 * medium_vars['N2'] >= 30000, "Online Budget At Least $30,000"

prob.writeLP("solutions/AdvertisingCampaign.lp")
prob.solve()

print(f"Status: {LpStatus[prob.status]}")
def get_value(r, d):
    return int(prob.variables()[r].varValue + prob.variables()[d].varValue)

for v in prob.variables():
    print(f"{v.name} = {v.varValue}")
print("\n")
print(f"TV Ads: {get_value(4, 5)}")
print(f"Radio Ads: {get_value(2, 3)}")
print(f"Online Ads: {get_value(0, 1)}")

print(f"Total Exposure Rating: {value(prob.objective)}")