def slices(series, length):
    if(length == 0):
        raise ValueError("slice length cannot be zero")
    if(length < 0):
        raise ValueError("slice length cannot be negative")
    if(series == ""):
        raise ValueError("series cannot be empty")
    if(length > len(series)):
        raise ValueError("slice length cannot be greater than series length")
    result = []
    for i in range(len(series)+1-length):
        result.append(series[i:i+length])
    return result
