def transform(legacy_data: dict):
    new_data = {}
    for point, letters in legacy_data.items():
        new_data |= {l.lower(): point for l in letters}
    return new_data
