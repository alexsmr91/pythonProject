def convert_time(duration: int) -> str:
    if duration > 0:
        st = str(duration % 60) + ' сек'
        duration = duration // 60
        if duration > 0:
            st = str(duration % 60) + ' мин ' + st
            duration = duration // 60
            if duration > 0:
                st = str(duration % 24) + ' час ' + st
                duration = duration // 24
                if duration > 0:
                    st = str(duration) + ' дн ' + st
    else:
        st = 'ошибка'
    return st

"""
dur_dur = [-1,53,153,4153,400153]

for i in range(len(dur_dur)):
    print (convert_time(dur_dur[i]))
"""

duration = 153
result = convert_time(duration)
print(result)


