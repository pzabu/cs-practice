import json


def csv_to_records(text: str) -> list[dict]:
    if not text:
        return []
    lines = text.split('\n')
    while lines and lines[-1] == '':
        lines.pop()
    if not lines:
        return []
    headers = [h.strip() for h in lines[0].split(',')]
    records = []
    for line in lines[1:]:
        if not line:
            continue
        values = [v.strip() for v in line.split(',')]
        records.append(dict(zip(headers, values)))
    return records


def _parse_yaml_value(s: str):
    s = s.strip()
    if not s:
        return s
    low = s.lower()
    if low in ('true', 'yes'):
        return True
    if low in ('false', 'no'):
        return False
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_key = None
    for line in lines:
        if '#' in line:
            line = line[:line.index('#')]
        stripped = line.strip()
        if not stripped:
            continue
        if ':' in stripped:
            idx = stripped.index(':')
            key = stripped[:idx].strip()
            value_part = stripped[idx + 1:].strip()
            if value_part == '':
                current_key = key
                result[key] = []
            else:
                result[key] = _parse_yaml_value(value_part)
                current_key = None
        elif stripped.startswith('- '):
            value = stripped[2:].strip()
            if current_key is not None:
                result[current_key].append(_parse_yaml_value(value))
    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    return [
        {**extra.get(row.get(key), {}), **row}
        for row in rows
    ]


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False)
