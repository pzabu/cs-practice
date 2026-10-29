import json
def csv_to_records(text):
    zag = text[0].split(',')
    a = []
    for t in range(len(text.split())-1):
        d = dict()      
        ts = text[t].split(',')  
        for x,tau in zip(zag,ts):
            d[x] = d.get(tau)
        a.append(d)
    return a

def parse_settings(lines):
    d = dict()
    f = False
    cur_zag = ''
    for i in range(len(lines)-1):
        l = lines[i]
        if l[0] == "#":
            continue
        f = True
        if ':' in l:       
            l = l.split(':')
            if len(l) == 2:
                d[l[0]] = d.get(l[1])
            else:
                cur_zag = l[0]
        else:
            d[cur_zag] = d.get(l)
    if f:
        return d
    return None

def merge_by_key(rows, extra, key):
    return [
        {**extra.get(row.get(key), {}), **row}
        for row in rows
    ]
def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False)
