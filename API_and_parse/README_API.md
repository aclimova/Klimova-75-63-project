# Работа с RCSB PDB Data API

**Описание:**  
Получение информации о структурах белков и ферментов через RCSB PDB Data API.

**Ссылка на API:**  
https://data.rcsb.org/rest/v1/core/entry/{pdb_id}

**Файлы проекта:**  
- `fetch_pdb_data.py` — запросы к API, возвращает данные по PDB ID  
- `parse_and_save_pdb.py` — парсер, формирует CSV из данных API  

**Категории, которые выводим:**  
- `id` — PDB ID  
- `title` — название структуры  
- `experimental_method` — метод определения структуры  

**Количество строк в CSV:**  
- Соответствует количеству PDB ID в списке (`pdb_ids`)  
- Пример: 10 PDB ID → CSV с 10 строками  

![Пример вывода первых 10 строк](https://github.com/user-attachments/assets/75684cd8-66f8-4add-b8a3-bc29c0822dfd)


