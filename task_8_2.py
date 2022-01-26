import re
import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов """
    RE_ADDR = re.compile(r'(([0-9]{1,3}[\.]){3}[0-9]{1,3})|(((^|:)([0-9a-fA-F]{0,4})){1,8})')
    remote_addr = take_str(RE_ADDR.findall(line)[0])
    RE_TIME = re.compile(r'\d{1,2}\/\w+\/\d{4}(\:\d{2}){3}\s\+\d{4}')
    request_datetime = RE_TIME.search(line).group()
    RE_REQ = re.compile(r'\]\s\"\w+\s[\/|\w]+')
    reque = RE_REQ.findall(line)[0].split(' ')
    request_type = reque[1][1::]
    requested_resource = reque[2]
    RE_CS = re.compile(r'\d+\s\d+')
    recs = RE_CS.findall(line)[0].split()
    response_code = recs[0]
    response_size = recs[1]
    return (remote_addr if remote_addr else None,
            request_datetime if request_datetime else None,
            request_type if request_type else None,
            requested_resource if requested_resource else None,
            response_code if response_code else None,
            response_size if response_size else None)


if __name__ == '__main__':
    log_file = 'nginx_logs.txt'
    loggs = []

    with open(log_file, 'r', encoding='utf-8') as fr:
        for line in fr:
            tuup = get_parse_attrs(line)
            loggs.append(tuup)

        pprint.pprint(loggs)
