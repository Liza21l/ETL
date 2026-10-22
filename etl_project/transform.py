# Подвоєння значень у стовпці price
def transform_data(df):
    df = df.copy()
    df["double_price"] = df["price"] * 2
    return df


# Перевірка валідності даних з API
def validate_data(data, required_fields):
    if not isinstance(data, dict):
        return False

    for field in required_fields:
        if field not in data:
            return False

        if data[field] is None:
            return False

    return True