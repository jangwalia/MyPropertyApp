import requests

def get_realtor_data():
    url = 'https://api2.realtor.ca/Listing.svc/PropertySearch_Post'
    opts = {
        'LongitudeMin': -122.8884917, 
        'LongitudeMax': -122.7154137, 
        'LatitudeMin': 49.0160805, 
        'LatitudeMax': 49.0509935, 
        'PriceMin': 800000, 
        'PriceMax': 1200000,
        'CultureId': 1,
        'ApplicationId': 1,
        'PropertySearchTypeId': 1,
        'RecordsPerPage': 2
    }

    r = requests.post(url, opts)
    data = r.json()
    Resulted_property = []
    for property in data['Results']:
        filtered_property = {
        "Address" : property['Property']['Address']['AddressText'],
        "Longitude" : property['Property']['Address']['Longitude'],
        "Latitude" : property['Property']['Address']['Latitude'],
        "Picture" : property['Property']['Photo'][0]['LowResPath'],
        "URL" : 'https://www.realtor.ca' + property ['RelativeDetailsURL']
        
        }
        Resulted_property.append(filtered_property)

    return(Resulted_property)

