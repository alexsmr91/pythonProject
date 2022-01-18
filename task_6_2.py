

def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    pos = line.find(' ')
    remote_addr = line[:pos]
    pos = line.find('"') + 1
    pos_b = line.find(' ', pos)
    request_type = line[pos:pos_b]
    pos_b += 1
    pos = line.find(' ', pos_b)
    requested_resource = line[pos_b:pos]
    return (remote_addr if remote_addr else None,
            request_type if request_type else None,
            requested_resource if requested_resource else None) # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>



max_req = 0
spamers = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        addr, tp, res = get_parse_attrs(line)
        req_count = spamers.get(addr)
        if req_count:
            req_count += 1
            spamers[addr] = req_count
        else:
            req_count = spamers.setdefault(addr, 1)
        if req_count > max_req:
            spamer = addr
            max_req = req_count

print(f'IP спамера {spamer}, количество запросов {max_req}')

spamers_sort = {}
sorted_keys = sorted(spamers, key=spamers.get)
for w in sorted_keys:
    spamers_sort[w] = spamers[w]


#Топ лист спамеров
n = 5
print(f'\nТоп {n} спамеров')
for _ in range(n):
    print(spamers_sort.popitem())
