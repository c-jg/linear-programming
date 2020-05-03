\* UES_Assignment_Problem *\
Minimize
Total_Cost: 170 Routes_DB_1 + 185 Routes_DB_2 + 190 Routes_DB_3
 + 280 Routes_DB_4 + 270 Routes_LD_1 + 200 Routes_LD_2 + 130 Routes_LD_3
 + 260 Routes_LD_4 + 220 Routes_LF_1 + 190 Routes_LF_2 + 140 Routes_LF_3
 + 240 Routes_LF_4 + 210 Routes_MC_1 + 225 Routes_MC_2 + 135 Routes_MC_3
 + 260 Routes_MC_4 + 190 Routes_MP_1 + 175 Routes_MP_2 + 125 Routes_MP_3
 + 230 Routes_MP_4 + 150 Routes_SM_1 + 235 Routes_SM_2 + 155 Routes_SM_3
 + 220 Routes_SM_4
Subject To
Demand_Constraint_for_1: Routes_DB_1 + Routes_LD_1 + Routes_LF_1 + Routes_MC_1
 + Routes_MP_1 + Routes_SM_1 = 1
Demand_Constraint_for_2: Routes_DB_2 + Routes_LD_2 + Routes_LF_2 + Routes_MC_2
 + Routes_MP_2 + Routes_SM_2 = 1
Demand_Constraint_for_3: Routes_DB_3 + Routes_LD_3 + Routes_LF_3 + Routes_MC_3
 + Routes_MP_3 + Routes_SM_3 = 1
Demand_Constraint_for_4: Routes_DB_4 + Routes_LD_4 + Routes_LF_4 + Routes_MC_4
 + Routes_MP_4 + Routes_SM_4 = 1
Supply_Constraint_for_DB: Routes_DB_1 + Routes_DB_2 + Routes_DB_3
 + Routes_DB_4 <= 1
Supply_Constraint_for_LD: Routes_LD_1 + Routes_LD_2 + Routes_LD_3
 + Routes_LD_4 <= 1
Supply_Constraint_for_LF: Routes_LF_1 + Routes_LF_2 + Routes_LF_3
 + Routes_LF_4 <= 1
Supply_Constraint_for_MC: Routes_MC_1 + Routes_MC_2 + Routes_MC_3
 + Routes_MC_4 <= 1
Supply_Constraint_for_MP: Routes_MP_1 + Routes_MP_2 + Routes_MP_3
 + Routes_MP_4 <= 1
Supply_Constraint_for_SM: Routes_SM_1 + Routes_SM_2 + Routes_SM_3
 + Routes_SM_4 <= 1
Bounds
0 <= Routes_DB_1
0 <= Routes_DB_2
0 <= Routes_DB_3
0 <= Routes_DB_4
0 <= Routes_LD_1
0 <= Routes_LD_2
0 <= Routes_LD_3
0 <= Routes_LD_4
0 <= Routes_LF_1
0 <= Routes_LF_2
0 <= Routes_LF_3
0 <= Routes_LF_4
0 <= Routes_MC_1
0 <= Routes_MC_2
0 <= Routes_MC_3
0 <= Routes_MC_4
0 <= Routes_MP_1
0 <= Routes_MP_2
0 <= Routes_MP_3
0 <= Routes_MP_4
0 <= Routes_SM_1
0 <= Routes_SM_2
0 <= Routes_SM_3
0 <= Routes_SM_4
Generals
Routes_DB_1
Routes_DB_2
Routes_DB_3
Routes_DB_4
Routes_LD_1
Routes_LD_2
Routes_LD_3
Routes_LD_4
Routes_LF_1
Routes_LF_2
Routes_LF_3
Routes_LF_4
Routes_MC_1
Routes_MC_2
Routes_MC_3
Routes_MC_4
Routes_MP_1
Routes_MP_2
Routes_MP_3
Routes_MP_4
Routes_SM_1
Routes_SM_2
Routes_SM_3
Routes_SM_4
End
