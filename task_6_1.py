from pprint import pprint



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




list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    list_out = [get_parse_attrs(line) for line in fr]  # передавайте данные в функцию и наполняйте список list_out кортежами

pprint(list_out)

