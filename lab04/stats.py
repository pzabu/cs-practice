import sys
def parse_record(line):
    d = {}
    if line.count(';')<3: raise ValueError("Полей не ровно 3")
    c, t, date = line.split(";")    
    if !c or !date:
        raise ValueError("Город или дата пустые")
    d['city'] = c
    try: 
        d['temperature'] = float(t)
    except ValueError:
        raise ValueError("Температура не число")
    d['date'] = date
    return d
def read_valid(lines):
    res = []
    for line in lines:
        try:
            res.append(parse_record(line))
        except ValueError:
            continue
    return res
def average_by_city(records):
    total = {}
    counts = {}
    for dict1 in records:
        total[dict1['city']] = total.get(dict1['city'], 0) + dict1['temperature']
        counts[dict1['city']] = counts.get(dict1['city'], 0) + 1
    result = {}
    for t1 in total:
        result[t1] = total[t1]/counts[t1]
    return result
def warmest_city(records):
    avg = average_by_city(records)
    best = ""
    for city in avg:
        if best == "" or avg[city] < avg[best] or (avg[city] == avg[best] and city<best):
            best = city
    return best


