from requests import *
import json


def get_cat():
    try:
        response = get("https://api.thecatapi.com/v1/images/search?&breed_ids=munchkin")
    except ConnectionError:
        print("Проверьте подключение к сети.")
    else:
        response = json.loads(response.content)
        img_url = response[0]['url']
        print(response)
        print(img_url)
        return img_url
 #        img_data = get(img_url).content
 #        with open('cat.png', 'wb') as file:
 #            file.write(img_data)
