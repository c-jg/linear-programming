\* JD_Williams_Investment_Strategy_Problem *\
Maximize
Total_Yield: 0.18 Fund_GROWTH + 0.125 Fund_INCOME + 0.075 Fund_MONEY_MARKET
Subject To
Amount_Invested_in_Growth_Fund_<=_40%: Fund_GROWTH <= 0.4
Amount_Invested_in_Growth_Fund_>=_20%: Fund_GROWTH >= 0.2
Amount_Invested_in_Income_Fund_<=_50%: Fund_INCOME <= 0.5
Amount_Invested_in_Income_Fund_>=_20%: Fund_INCOME >= 0.2
Amount_Invested_in_Money_Market_Fund_At_Least_30%: Fund_MONEY_MARKET >= 0.3
Total_Invested: Fund_GROWTH + Fund_INCOME + Fund_MONEY_MARKET = 1
Total_Risk: 0.1 Fund_GROWTH + 0.07 Fund_INCOME + 0.01 Fund_MONEY_MARKET
 <= 0.05
End
