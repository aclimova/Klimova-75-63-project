import requests

def fetch_character_data(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text 

if __name__ == "__main__":
    json_str = fetch_character_data(108)
    with open("character_108.json", "w", encoding="utf-8") as f:
        f.write(json_str)
    print("Данные загружены и сохранены в character_108.json")
