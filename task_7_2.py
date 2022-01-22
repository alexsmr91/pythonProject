import os


class ConfError(Exception):
   pass


def read_conf(config_path='config.yaml') -> list:
    res_list = list()
    with open(config_path, 'r', encoding='utf-8') as f1:
        for line in f1:
            line = line.strip()
            if line:
                line_lvl = line.count('-')
                line = line.strip('-')
                d_f_pref = line[0:2].capitalize()
                if d_f_pref == 'F:' or d_f_pref == 'D:':
                    file_flag = (True if d_f_pref == 'F:' else False)
                else:
                    raise ConfError(f'Config error : in line "{line}" miss D: or F: sign (dir or file?)')
                line = line[2:].lower()
                res_list.append((line, file_flag, line_lvl))
            #else:
            #    raise ConfError(f'Config error : empty line')
    return res_list


def mk_dirs_files(prev_path: str, prev_flag: bool, prev_lvl: int, rem_list: list):
    if rem_list:
        cur_name, cur_flag, cur_lvl = rem_list[0]
        delta_lvl = prev_lvl - cur_lvl
        if delta_lvl == 0 and not prev_flag:
            res_path = os.path.join(prev_path, cur_name)
        elif delta_lvl == 0 and prev_flag:
            raise ConfError(f'Prev file "{prev_path}" cant be parent of current dir\\file "{cur_name}"')
        elif delta_lvl > 0:
            res_path = os.path.dirname(prev_path)
            for _ in range(delta_lvl-1):
                res_path = os.path.dirname(res_path)
            res_path = os.path.join(res_path, cur_name)
        elif delta_lvl < 0:
            raise ConfError(f'Prev path "{prev_path}", current dir\\file name "{cur_name}" dont have parrent')
        if not os.path.exists(res_path):
            if cur_flag:
                f = open(res_path, 'a')
                f.close()
            else:
                os.mkdir(res_path)
        mk_dirs_files(res_path, cur_flag, cur_lvl + 1, rem_list[1:])
    else:
        return


def starter():
    mk_dirs_files('', False, 0, read_conf())


starter()
