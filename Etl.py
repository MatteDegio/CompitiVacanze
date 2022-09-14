def transform(legacy_data):
    numero = {}
    for k in legacy_data:
        for j in legacy_data[k]:
            numero[j.lower()] = k
    return numero