import pandas as pd
import os

FILE_ID = "1U3DpetAYEV6RiAhVdqMXeu1nmz0C45ec"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

def load_data():
    try:
        df = pd.read_csv(file_url)
        print("Файл загружен\n")
        
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        print(df)
        
        df = df.drop_duplicates()
        
        numeric_cols = ['dbh', 'wood', 'bark', 'root', 'rootsk', 'branch']
        categorical_cols = ['species', 'fac26']
        
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        
        for col in categorical_cols:
            df[col] = df[col].astype('category')
            df[col] = df[col].cat.add_categories(['Unknown'])
            df[col] = df[col].fillna('Unknown')
        
        if not os.path.exists("data"):
            os.makedirs("data")
        df.to_csv("data/downloaded_dataset.csv", index=False)
        df.to_parquet("data/dataset_converted.parquet", index=False)
        print("\nДанные успешно сохранены в папке 'data' (CSV и Parquet).")
        
        print("\nТипы колонок после приведения")
        print(df.dtypes)
        
        return df
    
    except Exception as e:
        print("Ошибка при загрузке или обработке данных", e)
        return None

if __name__ == "__main__":
    df = load_data()
