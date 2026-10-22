from extract import extract_csv, extract_api
from transform import transform_data, validate_data
from load import load_parquet, load_database


def main():
    # 1. EXTRACT: отримання даних із CSV
    print("Завантаження CSV...")

    df = extract_csv("data.csv")

    print(df)

    # 2. TRANSFORM: обробка даних
    print("\nТрансформація даних...")

    df = transform_data(df)

    print(df)

    # 3. LOAD: збереження у Parquet
    print("\nЗбереження у Parquet...")

    load_parquet(df, "result.parquet")

    print("Файл result.parquet успішно створено.")

    # 4. LOAD: збереження у базу даних
    load_database(df)

    print("Дані збережено у SQLite.")

    # 5. EXTRACT: отримання даних з API
    print("\nОтримання даних з API...")

    url = "https://jsonplaceholder.typicode.com/todos/1"

    data = extract_api(url)

    # 6. TRANSFORM: перевірка валідності JSON
    required_fields = ["userId", "id", "title", "completed"]

    if validate_data(data, required_fields):
        print("Дані API валідні:")
        print(data)
    else:
        print("Помилка: дані API не пройшли перевірку.")


if __name__ == "__main__":
    main()