import requests
import json

def find_highest_superhero(sex,is_employed):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    if response.status_code == 200:
        heroes_data = response.json()
    else:
        print("error", response.status_code)
        return response.status_code
    highest_superhero_height = 0
    highest_superhero = None
    for i in heroes_data:
        current_hero_height = 0
        if i["appearance"]["gender"] == f"{sex}":
            if is_employed == 1 and i["work"]["occupation"] not in ("","-") and i["appearance"]["height"][0] not in ("","-"):
                height_info = (i["appearance"]["height"][1].split())
                if height_info[1] =="cm":
                    current_hero_height = float(height_info[0])
                elif height_info[1] == "meters":
                    current_hero_height = float(height_info[0]) * 100
                if current_hero_height > highest_superhero_height:
                    highest_superhero_height = current_hero_height
                    highest_superhero = i
            elif is_employed == 0 and i["work"]["occupation"] in ("","-") and i["appearance"]["height"][0] not in ("","-"):
                height_info = (i["appearance"]["height"][1].split())
                if height_info[1] =="cm":
                    current_hero_height = float(height_info[0])
                elif height_info[1] == "meters":
                    current_hero_height = float(height_info[0]) * 100
                if current_hero_height > highest_superhero_height:
                    highest_superhero_height = current_hero_height
                    highest_superhero = i
                #print((i["appearance"]["height"][0]))
    if highest_superhero is not None:
        return highest_superhero
    else:
        return None
print(find_highest_superhero("Male",1))