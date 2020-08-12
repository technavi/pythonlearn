import requests
import json

def main():
    response=requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson')
    data=response.json()
    print(response.status_code)
   # if(response.status_code==200):
      #  print(data)
    for item in data["features"]:
        print(item["properties"]["place"])
        print(item["properties"]["felt"])
main()