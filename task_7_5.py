import os
import json

scan_dir = 'some_data'
root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), scan_dir)
sz_dict = {}
for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        stat = os.stat(os.path.join(root, file))
        sz = stat.st_size
        deg = (0 if sz == 0 else 1)
        while sz > 10:
            sz = sz // 10
            deg = deg + 1
        key = (10 ** deg if deg > 0 else 0)
        val, ext_list = sz_dict.setdefault(key, (0, list()))
        if not ext_list.count(ext):
            ext_list.append(ext)
        sz_dict[key] = (val + 1, ext_list)


with open(f'{scan_dir}_summary.json', 'w', encoding='utf-8') as f1:
    json.dump(sz_dict, f1)
