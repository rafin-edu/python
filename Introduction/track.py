import phonenumbers,opencage,folium,webbrowser,os
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

number = input("Enter your number including country code:")

pepnumber = phonenumbers.parse(number)

#country
country = geocoder.description_for_number(pepnumber,"en")
print(country)

#service provider
service_pro = carrier.name_for_number(pepnumber,"en")
print(service_pro)

#location
oc_key = input("Enter your opencage api key:")
geocod = OpenCageGeocode(oc_key)
query = str(country)
result = geocod.geocode(query)
print(result)

#mapview
lat = result[0]["geometry"]['lat']
lng = result[0]["geometry"]['lng']
print(lat,lng)
my_map = folium.Map(location=[lat,lng],zoom_start= 15)
folium.Marker([lat,lng],popup=country).add_to(my_map)
my_map.save("Location.html")
webbrowser.open(f"file:///{os.getcwd()}/Location.html")