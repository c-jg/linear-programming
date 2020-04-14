'''
J. D. Williams, Inc. Investment Strategy Problem
'''

from pulp import *

FUNDS = ['GROWTH', 'INCOME', 'MONEY_MARKET']

INVEST_PERCENT = [[.2, .4],[.2, .5], [.3, 1]] 

RISK = {
    'GROWTH': .1,
    'INCOME': .07,
    'MONEY_MARKET': .01
}

# $800,000 invested 
YIELD = {
    'GROWTH': .18,
    'INCOME': .125,
    'MONEY_MARKET': .075
}

prob = LpProblem("JD Williams Investment Strategy Problem", LpMaximize)

fund_vars = LpVariable.dicts("Fund", FUNDS, 0)

# obj. function
prob += lpSum([YIELD[f] * fund_vars[f] for f in FUNDS]), "Total Yield"

# constraints
prob += fund_vars['GROWTH'] >= .2, "Amount Invested in Growth Fund >= 20%"
prob += fund_vars['GROWTH'] <= .4, "Amount Invested in Growth Fund <= 40%"
prob += fund_vars['INCOME'] >= .2, "Amount Invested in Income Fund >= 20%"
prob += fund_vars['INCOME'] <= .5, "Amount Invested in Income Fund <= 50%"
prob += fund_vars['MONEY_MARKET'] >= .3, "Amount Invested in Money Market Fund At Least 30%"
prob += lpSum([RISK[f] * fund_vars[f] for f in FUNDS]) <= .05, "Total Risk"
prob += lpSum([fund_vars[f] for f in FUNDS]) == 1, "Total Invested"

prob.writeLP("InvestmentStrategy.lp")
prob.solve()
print(f"Status: {LpStatus[prob.status]}")

for v in prob.variables():
    print(f"{v.name}% = {round(v.varValue * 100, 2)}%")

print(f"Total Return: ${round(value(prob.objective) * 800000, 2)}")
