import pandas as pd
import requests
import json


# Завантаження даних із CSV
def extract_csv(file_path):
    return pd.read_csv(file_path)


# Отримання даних з API
def extract_api(url, json_path="intermediate.json"):
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    # Зберігаємо проміжні результати у JSON
    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return data