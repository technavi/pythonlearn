import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=New-Delhi")
# print(response) 
print(response.status_code)  
# if(response.status_code=="200"):
soup=BeautifulSoup(response.content,"html.parser")
# print(soup.prettify())

cards=soup.find_all("div",attrs={"class":"m-srp-card__container"})
for card in cards:
    price= card.find("div",attrs={"class":"m-srp-card__price"})
    title= card.find("span",attrs={"class":"m-srp-card__title__bhk"})
    # print(title.text)
    print("Property '{}' and its price is '{}'".format(title.text.strip("\n"), price.text))
