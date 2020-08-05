import googlemaps
import csv
import json
import time

next = None

api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"
placeList = []
gmaps = googlemaps.Client(key=api_key)

try:
    query_result = gmaps.places_nearby(
            location = (38.897957, -77.036560),
            radius=10000, type = 'restaurant', min_price = 2, page_token = next)
    new_query =    gmaps.places_nearby(
                location = (38.9079, -76.8297),
                radius=10000, type = 'restaurant', min_price = 2, page_token = next)
except ApiError as e:
    print(e)
else:
    num = 0
    for place in query_result['results']:
        my_place_id = place['place_id']
        myfields = ['name', 'business_status','price_level','rating']
        place_details = gmaps.place(place_id = my_place_id, fields = myfields)
        placeList.append(place_details)


    for place in new_query['results']:
        my_place_id = place['place_id']
        myfields = ['name', 'business_status','price_level','rating']
        place_details = gmaps.place(place_id = my_place_id, fields = myfields)
        placeList.append(place_details)

time.sleep(2)

try:
    query_result['next_page_token']
    new_query['next_page_token']
except KeyError as e:
    print('complete')

columns = ['Name', 'Price Level', 'Rating', 'Status']
with open('restaurants.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    for item in placeList:
        writer.writerow([item['result']['name'], item['result']['price_level'],item['result']['rating'], item['result']['business_status']])
