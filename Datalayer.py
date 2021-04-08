import requests
class Network:
    def __init__(self):
        print('Networking Started')
    def search(self,entityid):
        try:
            print('https://services.odata.org/TripPinRESTierService/People(\'{0}\')'.format(entityid))
            resp = requests.get('https://services.odata.org/TripPinRESTierService/People(\'{0}\')'.format(entityid))
            if resp.status_code == 200:
                return resp.json()

        except requests.exceptions.HTTPError as err:
            print('error encountered ',err)
            raise err
    def filter(self,filterid):
        try:
            print('https://services.odata.org/TripPinRESTierService/People?$filter=FirstName eq \'{0}\''.format(filterid))
            resp = requests.get('https://services.odata.org/TripPinRESTierService/People?$filter=FirstName eq \'{0}\''.format(filterid))
            if resp.status_code == 200:
                return resp.json()

        except requests.exceptions.HTTPError as err:
            print('error encountered ',err)
            raise err

    def create(self,body):
        try:

            resp = requests.post('https://services.odata.org/TripPinRESTierService/People',data=body)
            if resp.status_code == 200:
                return resp.json()

        except requests.exceptions.HTTPError as err:
            print('error encountered ',err)
            raise err
