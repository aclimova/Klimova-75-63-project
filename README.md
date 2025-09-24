# Klimova-75-63-project
О проекте

Проект посвящён обработке и анализу уникального датасета древесных характеристик.
Основные задачи проекта:

Загрузка данных из внешнего источника (Google Drive)

Очистка данных: удаление дубликатов, обработка пропусков

Приведение типов колонок (числовые и категориальные)

Сохранение обработанных данных в форматах CSV и Parquet

Визуальный и статистический анализ данных (EDA)

Структура репозитория
your_project_name/
│
├─ data/                  # Исходные и обработанные данные
│   ├─ dataset_raw.parquet
│   ├─ dataset_processed.parquet
│   └─ downloaded_dataset.csv
│
├─ notebooks/             # Jupyter ноутбуки для анализа и визуализации
│   ├─ 01_data_exploration.ipynb
│   └─ 02_analysis.ipynb
│
├─ src/                   # Скрипты Python
│   └─ data_processing.py
│
├─ requirements.txt       # Список зависимостей
├─ README.md              # Описание проекта
└─ .gitignore             # Игнорируем лишние файлы

Установка и запуск

Клонируйте репозиторий:

git clone <ссылка на репо>


Создайте и активируйте виртуальное окружение:

conda create -n myenv python=3.11
conda activate myenv


Установите зависимости:

pip install -r requirements.txt


Запустите Jupyter Notebook:

jupyter notebook


В ноутбуке можно загрузить и обработать данные:

from src.data_processing import load_and_process_data
df = load_and_process_data()

Примечания

Визуализации строятся в ноутбуках из папки notebooks/

Все обработанные файлы сохраняются в папке data/

Пропуски в числовых колонках заменяются медианой, в категориальных – 'Unknown'

Ссылка на датасет: [Biomass Data](https://drive.google.com/drive/folders/1TOftr_GOVv2wXgeg4S5GTd46YWDHC2Ls?usp=drive_link) 

Домашнее задание №2

<img width="795" height="620" alt="screenshot" src="https://github.com/user-attachments/assets/345ff719-20e7-4dff-99b9-a32712106360" />
