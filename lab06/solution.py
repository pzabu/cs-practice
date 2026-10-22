def count_by_extension(paths):
    res = {}
    for part in paths:
        part = part.lower()
        if part.count('.')!= 1:
            continue
        key = part.split('.')[-1]
        res[key] = res.get(key, 0) + 1
    return res

def deepest_path(paths):
    ghoul = ''
    for l in paths:
        if l.count('/') > ghoul.count('/'):
            res = l
        elif l.count('/') == ghoul.count('/'):
            if l < ghoul:
                ghoul = l
    return ghoul



