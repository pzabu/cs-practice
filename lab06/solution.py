def count_by_extension(paths):
    res = {}
    for part in paths:
        part = part.lower()
        if part.count('.')!= 1:
            continue
        key = part.split('.')[-1]
        res[key] = res.get(key, 0) + 1
    return res



