import requests
import csv
import json

def get_realtor_data(minimum=800000,maximum=1000000):
    
    url = 'https://api2.realtor.ca/Listing.svc/PropertySearch_Post'
    opts = {
        'LongitudeMin': -122.8884917, 
        'LongitudeMax': -122.7154137, 
        'LatitudeMin': 49.0160805, 
        'LatitudeMax': 49.0509935, 
        'PriceMin':minimum, 
        'PriceMax':maximum,
        'CultureId': 1,
        'ApplicationId': 1,
        'PropertySearchTypeId': 1,
        'RecordsPerPage': 2
    }

    r = requests.post(url, opts)
    try:
        data = r.json()
        
    except json.decoder.JSONDecodeError:
        print('There was a problem fetching API Data...')
        with open('data/realtordata.json',mode = 'r') as jsonfile:
            data = json.load(jsonfile)
            return data
    
    else:
        print('Sucessfully loaded data')
    
    finally:
        Resulted_property = []
        for property in data['Results']:
            filtered_property = {
            "Price": property['Property']['Price'],
            "Address" : property['Property']['Address']['AddressText'],
            "Longitude" : property['Property']['Address']['Longitude'],
            "Latitude" : property['Property']['Address']['Latitude'],
            "Picture" : property['Property']['Photo'][0]['LowResPath'],
            "URL" : 'https://www.realtor.ca'+ property['RelativeDetailsURL']
            
            }
            Resulted_property.append(filtered_property)

        return(Resulted_property)

def get_csv_data(filepath):
    assessment_data = []
    with open(filepath,mode='r') as csvfile:
      content   = csv.DictReader(csvfile)
      for row in content:
        assessment_data.append(row)
    
    return(assessment_data)

def set_markers(property_list):
    markers = []
    
    for property_map in property_list:
        icon = ''
        if int(property_map['Price'].strip("$").replace(',' ,'')) < 808500:
            icon = 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
        else:
            icon = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
        marker = {
            'icon' : icon,
            'lat' : property_map['Latitude'],
            'lng' : property_map['Longitude'],
            'infobox' :property_map['Price'] + '<br>'  + property_map['Address'] + '<br>' + '<a href = ' +  property_map['URL'] +'><p>Click here to view detail</p></a><br><img src = ' + property_map['Picture'] + '>'
            }
        markers.append(marker)
    return markers



