**The project is driven by Usercommand.py file **
Run Usercommand.py
Command = python Usercommand.py --UserName | -- Filter | -- Create  (anyone of these parameters is to be provided)
Example : python Usercommand.py --UserName russellwhyte

--UserName parameter to call : GET https://services.odata.org/TripPinRESTierService/People('****')
-- Filter parameter to call : https://services.odata.org/TripPinRESTierService/People?$filter=FirstName eq '***'
__ Create parameter to call : https://services.odata.org/TripPinRESTierService/People
*** Create parameter accepts dictionary as user input with proper escaping only

Responses are logged in Strata.log