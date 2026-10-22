import sqlite3


# Збереження таблиці у форматі Parquet
def load_parquet(df, file_path):
    df.to_parquet(file_path, index=False)


# Збереження даних у базу SQLite
def load_database(df, table_name="products"):
    connection = sqlite3.connect("etl_database.db")

    try:
        df.to_sql(
            table_name,
            connection,
            if_exists="replace",
            index=False
        )
    finally:
        connection.close()