\* Foster_Generators_Practice_Transportation_Problem *\
Minimize
Sum_of_Transporting_Costs: 7 Route_Bedford_Boston + 5 Route_Bedford_Chicago
 + 3 Route_Bedford_Lexington + 2 Route_Bedford_St._Louis
 + 3 Route_Cleveland_Boston + 2 Route_Cleveland_Chicago
 + 6 Route_Cleveland_Lexington + 7 Route_Cleveland_St._Louis
 + 2 Route_York_Boston + 5 Route_York_Chicago + 5 Route_York_Lexington
 + 4 Route_York_St._Louis
Subject To
Sum_of_Shipment_From_Bedford: Route_Bedford_Boston + Route_Bedford_Chicago
 + Route_Bedford_Lexington + Route_Bedford_St._Louis <= 6000
Sum_of_Shipment_From_Cleveland: Route_Cleveland_Boston
 + Route_Cleveland_Chicago + Route_Cleveland_Lexington
 + Route_Cleveland_St._Louis <= 5000
Sum_of_Shipment_From_York: Route_York_Boston + Route_York_Chicago
 + Route_York_Lexington + Route_York_St._Louis <= 2500
Sum_of_Shipment_into_Boston: Route_Bedford_Boston + Route_Cleveland_Boston
 + Route_York_Boston = 6000
Sum_of_Shipment_into_Chicago: Route_Bedford_Chicago + Route_Cleveland_Chicago
 + Route_York_Chicago = 4000
Sum_of_Shipment_into_Lexington: Route_Bedford_Lexington
 + Route_Cleveland_Lexington + Route_York_Lexington = 1500
Sum_of_Shipment_into_St._Louis: Route_Bedford_St._Louis
 + Route_Cleveland_St._Louis + Route_York_St._Louis = 2000
Bounds
0 <= Route_Bedford_Boston
0 <= Route_Bedford_Chicago
0 <= Route_Bedford_Lexington
0 <= Route_Bedford_St._Louis
0 <= Route_Cleveland_Boston
0 <= Route_Cleveland_Chicago
0 <= Route_Cleveland_Lexington
0 <= Route_Cleveland_St._Louis
0 <= Route_York_Boston
0 <= Route_York_Chicago
0 <= Route_York_Lexington
0 <= Route_York_St._Louis
Generals
Route_Bedford_Boston
Route_Bedford_Chicago
Route_Bedford_Lexington
Route_Bedford_St._Louis
Route_Cleveland_Boston
Route_Cleveland_Chicago
Route_Cleveland_Lexington
Route_Cleveland_St._Louis
Route_York_Boston
Route_York_Chicago
Route_York_Lexington
Route_York_St._Louis
End
