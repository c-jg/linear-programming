\* Advertising_Campaign_Problem *\
Maximize
Total_Exposure_Rating: 10 Media_N1 + 5 Media_N2 + 25 Media_R1 + 20 Media_R2
 + 90 Media_T1 + 55 Media_T2
Subject To
No_More_Than_20_TV_Ads: Media_T1 + Media_T2 <= 20
Online_Budget_At_Least_$30,000: 1000 Media_N1 + 1000 Media_N2 >= 30000
Radio_Budget_Max:_$99,000: 3000 Media_R1 + 3000 Media_R2 <= 99000
Reliable_Online: Media_N1 <= 20
Reliable_Radio: Media_R1 <= 15
Reliable_TV: Media_T1 <= 10
TV_Budget_At_Least_$140,000: 10000 Media_T1 + 10000 Media_T2 >= 140000
Total_Budget: 1000 Media_N1 + 1000 Media_N2 + 3000 Media_R1 + 3000 Media_R2
 + 10000 Media_T1 + 10000 Media_T2 <= 279000
Total_New_Customers: 1000 Media_N1 + 800 Media_N2 + 2000 Media_R1
 + 1200 Media_R2 + 4000 Media_T1 + 1500 Media_T2 >= 100000
Twice_As_Many_Radio_Ads_As_TV: - Media_R1 - Media_R2 + 2 Media_T1 + 2 Media_T2
 <= 0
End
