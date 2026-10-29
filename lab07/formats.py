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


