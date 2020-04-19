\* Schneider's_Sweet_Shop_Ice_Cream_Blending_Problem *\
Minimize
Total_Cost_of_Batch: 1.19 Ingredient_X1 + 1.75 Ingredient_X10
 + 4.45 Ingredient_X11 + 2.45 Ingredient_X12 + 1.68 Ingredient_X13
 + 0.7 Ingredient_X2 + 2.32 Ingredient_X3 + 2.3 Ingredient_X4
 + 2.87 Ingredient_X5 + 0.25 Ingredient_X6 + 0.35 Ingredient_X7
 + 0.65 Ingredient_X8 + 0.25 Ingredient_X9
Subject To
Egg_Solids_High: 0.4 Ingredient_X10 + 0.4 Ingredient_X11 <= 0.2
Egg_Solids_Low: 0.4 Ingredient_X10 + 0.4 Ingredient_X11 >= 0.15
Emulsifier_High: Ingredient_X13 <= 0.1
Emulsifier_Low: Ingredient_X13 >= 0.05
Fat_High: 0.4 Ingredient_X1 + 0.5 Ingredient_X10 + 0.6 Ingredient_X11
 + 0.2 Ingredient_X2 + 0.8 Ingredient_X3 + 0.8 Ingredient_X4
 + 0.9 Ingredient_X5 + 0.1 Ingredient_X6 <= 8.5
Fat_Low: 0.4 Ingredient_X1 + 0.5 Ingredient_X10 + 0.6 Ingredient_X11
 + 0.2 Ingredient_X2 + 0.8 Ingredient_X3 + 0.8 Ingredient_X4
 + 0.9 Ingredient_X5 + 0.1 Ingredient_X6 >= 7.5
Serum_Solids_High: 0.1 Ingredient_X1 + 0.1 Ingredient_X4 + 0.1 Ingredient_X6
 + 0.3 Ingredient_X7 + Ingredient_X8 <= 4.5
Serum_Solids_Low: 0.1 Ingredient_X1 + 0.1 Ingredient_X4 + 0.1 Ingredient_X6
 + 0.3 Ingredient_X7 + Ingredient_X8 >= 3.5
Stabilizer_High: Ingredient_X12 <= 0.15
Stabilizer_Low: Ingredient_X12 >= 0.1
Sugar_Solids_High: 0.1 Ingredient_X10 + 0.7 Ingredient_X9 <= 8.25
Sugar_Solids_Low: 0.1 Ingredient_X10 + 0.7 Ingredient_X9 >= 7.75
Total_of_50_lbs: Ingredient_X1 + Ingredient_X10 + Ingredient_X11
 + Ingredient_X12 + Ingredient_X13 + Ingredient_X14 + Ingredient_X2
 + Ingredient_X3 + Ingredient_X4 + Ingredient_X5 + Ingredient_X6
 + Ingredient_X7 + Ingredient_X8 + Ingredient_X9 = 50
Water_High: 0.5 Ingredient_X1 + Ingredient_X14 + 0.8 Ingredient_X2
 + 0.2 Ingredient_X3 + 0.1 Ingredient_X4 + 0.1 Ingredient_X5
 + 0.8 Ingredient_X6 + 0.7 Ingredient_X7 + 0.3 Ingredient_X9 <= 29.75
Water_Low: 0.5 Ingredient_X1 + Ingredient_X14 + 0.8 Ingredient_X2
 + 0.2 Ingredient_X3 + 0.1 Ingredient_X4 + 0.1 Ingredient_X5
 + 0.8 Ingredient_X6 + 0.7 Ingredient_X7 + 0.3 Ingredient_X9 >= 29
End
