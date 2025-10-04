import requests
def fetch_pdb_data(pdb_ids):
    results = []
    for pdb_id in pdb_ids:
        print(f"Запрашиваем {pdb_id}...")
        url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            title = data.get("struct", {}).get("title", "без названия")
            method = data.get("exptl", [{}])[0].get("method", "не указан")
            print(f"Получено: {title} ({method})")
            results.append({
                "id": pdb_id,
                "title": title,
                "experimental_method": method
            })
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении {pdb_id}: {e}")
            results.append({
                "id": pdb_id,
                "title": None,
                "experimental_method": None
            })
    return results
