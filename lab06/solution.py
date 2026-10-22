def count_by_extension(paths):
    res = {}
    for part in paths:
        part = part.lower()
        if part.count('.')<1:
            continue
        key = part.split('.')[-1]
        if key == '':
            key = ' '
        res[key] = res.get(key, 0) + 1
    return res

def deepest_path(paths):
    ghoul = ''
    for l in paths:
        if l.count('/') > ghoul.count('/'):
            ghoul = l
        elif l.count('/') == ghoul.count('/') and l> ghoul:
            ghoul = l
    return ghoul

def human_size(n):
    sizes = ['Б','КБ','МБ','ГБ','ТБ']
    c =0    
    while n>=1024:
        n/=1024
        c+=1
    return f"{n} {sizes[c]}"

print(human_size(900))
print(human_size(1536))
print(human_size(5 * 1024 * 1024))

