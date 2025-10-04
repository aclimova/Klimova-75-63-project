import pandas as pd
from fetch_pdb_data import fetch_pdb_data

pdb_ids = [
    "4HHB", "1BNA", "2VYI", "6LU7", "1HVR",
    "2M6Q", "1AKI", "3LZM", "1A2P", "1TUP"
]

entries = fetch_pdb_data(pdb_ids)

if not entries:
    print("Нет данных для создания DataFrame")
    exit()

df = pd.DataFrame(entries)

print("\nРезультат в DataFrame:")
print(df.head(10))

df.to_csv("pdb_structures.csv", index=False)
print("\nДанные сохранены в pdb_structures.csv")
