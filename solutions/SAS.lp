\* Sports_of_All_Sorts_Transshipment *\
Minimize
Sum_of_Shipping_Costs: 27.5 Route_('AK',_'JSS') + 25 Route_('AK',_'SNS')
 + 42.5 Route_('AK',_'TSD') + 32.5 Route_('AS',_'AK') + 40 Route_('AS',_'IA')
 + 42.5 Route_('AS',_'ID') + 40 Route_('AS',_'MY') + 40 Route_('DT',_'AK')
 + 25 Route_('DT',_'IA') + 35 Route_('DT',_'ID') + 25 Route_('DT',_'MY')
 + 30 Route_('IA',_'JSS') + 27.5 Route_('IA',_'SNS') + 30 Route_('IA',_'TSD')
 + 35 Route_('ID',_'JSS') + 40 Route_('ID',_'SNS') + 32.5 Route_('ID',_'TSD')
 + 42.5 Route_('LA',_'AK') + 35 Route_('LA',_'IA') + 35 Route_('LA',_'ID')
 + 45 Route_('LA',_'MY') + 20 Route_('MY',_'JSS') + 32.5 Route_('MY',_'SNS')
 + 40 Route_('MY',_'TSD')
Subject To
Equal_Shipments_in/out_of_AK: - Route_('AK',_'JSS') - Route_('AK',_'SNS')
 - Route_('AK',_'TSD') + Route_('AS',_'AK') + Route_('DT',_'AK')
 + Route_('LA',_'AK') = 0
Equal_Shipments_in/out_of_IA: Route_('AS',_'IA') + Route_('DT',_'IA')
 - Route_('IA',_'JSS') - Route_('IA',_'SNS') - Route_('IA',_'TSD')
 + Route_('LA',_'IA') = 0
Equal_Shipments_in/out_of_ID: Route_('AS',_'ID') + Route_('DT',_'ID')
 - Route_('ID',_'JSS') - Route_('ID',_'SNS') - Route_('ID',_'TSD')
 + Route_('LA',_'ID') = 0
Equal_Shipments_in/out_of_MY: Route_('AS',_'MY') + Route_('DT',_'MY')
 + Route_('LA',_'MY') - Route_('MY',_'JSS') - Route_('MY',_'SNS')
 - Route_('MY',_'TSD') = 0
Sum_of_Shipment_from_AS: Route_('AS',_'AK') + Route_('AS',_'IA')
 + Route_('AS',_'ID') + Route_('AS',_'MY') <= 700
Sum_of_Shipment_from_DT: Route_('DT',_'AK') + Route_('DT',_'IA')
 + Route_('DT',_'ID') + Route_('DT',_'MY') <= 350
Sum_of_Shipment_from_LA: Route_('LA',_'AK') + Route_('LA',_'IA')
 + Route_('LA',_'ID') + Route_('LA',_'MY') <= 350
Sum_of_Shipments_to_AK: Route_('AS',_'AK') + Route_('DT',_'AK')
 + Route_('LA',_'AK') <= 500
Sum_of_Shipments_to_IA: Route_('AS',_'IA') + Route_('DT',_'IA')
 + Route_('LA',_'IA') <= 500
Sum_of_Shipments_to_ID: Route_('AS',_'ID') + Route_('DT',_'ID')
 + Route_('LA',_'ID') <= 500
Sum_of_Shipments_to_MY: Route_('AS',_'MY') + Route_('DT',_'MY')
 + Route_('LA',_'MY') <= 500
Sum_of_shipments_to_JSS: Route_('AK',_'JSS') + Route_('IA',_'JSS')
 + Route_('ID',_'JSS') + Route_('MY',_'JSS') = 200
Sum_of_shipments_to_SNS: Route_('AK',_'SNS') + Route_('IA',_'SNS')
 + Route_('ID',_'SNS') + Route_('MY',_'SNS') = 500
Sum_of_shipments_to_TSD: Route_('AK',_'TSD') + Route_('IA',_'TSD')
 + Route_('ID',_'TSD') + Route_('MY',_'TSD') = 650
Bounds
0 <= Route_('AK',_'JSS')
0 <= Route_('AK',_'SNS')
0 <= Route_('AK',_'TSD')
0 <= Route_('AS',_'AK')
0 <= Route_('AS',_'IA')
0 <= Route_('AS',_'ID')
0 <= Route_('AS',_'MY')
0 <= Route_('DT',_'AK')
0 <= Route_('DT',_'IA')
0 <= Route_('DT',_'ID')
0 <= Route_('DT',_'MY')
0 <= Route_('IA',_'JSS')
0 <= Route_('IA',_'SNS')
0 <= Route_('IA',_'TSD')
0 <= Route_('ID',_'JSS')
0 <= Route_('ID',_'SNS')
0 <= Route_('ID',_'TSD')
0 <= Route_('LA',_'AK')
0 <= Route_('LA',_'IA')
0 <= Route_('LA',_'ID')
0 <= Route_('LA',_'MY')
0 <= Route_('MY',_'JSS')
0 <= Route_('MY',_'SNS')
0 <= Route_('MY',_'TSD')
Generals
Route_('AK',_'JSS')
Route_('AK',_'SNS')
Route_('AK',_'TSD')
Route_('AS',_'AK')
Route_('AS',_'IA')
Route_('AS',_'ID')
Route_('AS',_'MY')
Route_('DT',_'AK')
Route_('DT',_'IA')
Route_('DT',_'ID')
Route_('DT',_'MY')
Route_('IA',_'JSS')
Route_('IA',_'SNS')
Route_('IA',_'TSD')
Route_('ID',_'JSS')
Route_('ID',_'SNS')
Route_('ID',_'TSD')
Route_('LA',_'AK')
Route_('LA',_'IA')
Route_('LA',_'ID')
Route_('LA',_'MY')
Route_('MY',_'JSS')
Route_('MY',_'SNS')
Route_('MY',_'TSD')
End
