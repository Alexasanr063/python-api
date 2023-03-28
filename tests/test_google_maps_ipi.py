import requests

class Dark():
    "Создание ссылки"
    def create_and_writind_new_acter(self):
        "create all jokes"
        base_url = "https://swapi.dev/api/"
        dark_v = "people/4/"

        films = (requests.get(base_url+dark_v)).json()
        list = []
        list2 =[]
    #получение имен актеров
        for elem in films.get("films"):
            character = requests.get(elem).json()
            characters = character.get("characters")
            for i in characters:
                text = requests.get(i).json().get("name")
                list.append(text)
    #Сортировка и запись актеров в файл
        fw = open('characters.txt', 'a', encoding="utf-8")
        for i in list:
            if i not in list2:
                list2.append(i)
                fw.write(i + '\n')
        fw.close()

random_acter = Dark()
random_acter.create_and_writind_new_acter()

