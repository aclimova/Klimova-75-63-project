import pandas as pd

FILE_ID = "1U3DpetAYEV6RiAhVdqMXeu1nmz0C45ec"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

try:
    raw_data = pd.read_csv(file_url)
    print("Файл загружен успешно!\n")
    print("Первые 10 строк данных:")
    print(raw_data.head(10).to_string(index=False))
    raw_data.to_csv("downloaded_dataset.csv", index=False)
    print("\nФайл сохранён")
    
except Exception as e:
    print("Ошибка:", e)
