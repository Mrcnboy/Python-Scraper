from bs4 import BeautifulSoup
import requests
import csv

def search_car (brand_search: str,energy: str,km_min: int,km_max: int,year_min: int,year_max: int,price_min: int,price_max: int):
    #Verification de l'espace ou non dans la marque
    if " " in brand_search:
        brand_search = brand_search.replace(" ", "%20")
    else:
        pass
    #Modification de la variable energie pour permettre la bonne requete dans l'url
    while energy == "essence" or energy == "diesel" or energy == "hybride" or energy == "electrique":
        if energy == "essence":
            energy = "ess"
        elif energy == "diesel":
            energy = "dies"
        elif energy == "hybrid":
            energy = "hyb"
        elif energy == "electrique":
            energy = "elec"
        else:
            energy = str(input("Merci d'entrer une energie"))
    #Maj de la variable pour mettre en majuscule
    brand_search = brand_search.upper()
    print(brand_search)
    #On ouvre le fichier info.csv ( si il n'est pas crée d'avance le script le crée en même temps )
    with open('info.csv', 'w', newline='') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow(['Brand', 'Model', 'Motor', 'Year','Fuel', 'Mileage','Price'])
        for number_page in range(1,20):
            url = f"https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand_search}&mileageMax={km_max}&mileageMin={km_min}&options=&page={number_page}&priceMax={price_max}&priceMin={price_min}&yearMax={year_max}&yearMin={year_min}"
            page = requests.get(url)
            print(url)
            soup = BeautifulSoup(page.content,'html.parser')
            lists = soup.findAll('div',class_="searchCard")
            i=0
            for list in lists :
                i+=1
                print("NEXT",i)
                brand = list.find('h3',
                                  class_="Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2")
                motor = list.find('div',
                                  class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2")
                year = list.findAll('div',
                                 class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")[0]
                price = list.find('span',
                                  class_="Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2")
                km = list.findAll('div',
                               class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")[1]
                fuel = list.findAll('div',
                                 class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")[3]
                if "%20" in brand_search:
                    brand_search = brand_search.replace("%20", " ")
                modele = brand.text.replace(brand_search, "")
                brand = str(brand.text)
                motor = str(motor.text)
                km = km.text.replace('\xa0',"")
                km = km.replace('km',"")
                km = int(km)
                price = price.text.replace('€',"")
                price = price.replace(" ","")
                price = int(price)
                info = [brand_search, modele, motor, year.text, fuel.text, km, price]
                print(info)
                writer.writerow(info)

__name__ = '__name__'
if __name__ == '__name__':
    search_car("renault","ess",1,160000,2015,2022,0,50000)