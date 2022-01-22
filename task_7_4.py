import os
import pprint

scan_dir = 'some_data'
root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), scan_dir)
sz_dict = {}
for root, dirs, files in os.walk(root_dir):
    for file in files:
        stat = os.stat(os.path.join(root, file))
        sz = stat.st_size
        deg = (0 if sz == 0 else 1)
        while sz > 10:
            sz = sz // 10
            deg = deg + 1
        key = (10 ** deg if deg > 0 else 0)
        val = sz_dict.setdefault(key, 0)
        sz_dict[key] = val + 1


pprint.pprint(sz_dict)
