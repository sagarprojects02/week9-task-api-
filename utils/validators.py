def validate_input(data, fields):
    return all(field in data for field in fields)
