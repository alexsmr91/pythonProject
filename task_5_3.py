
"""
def check_gen(tutors: list, klasses: list):
    i = 0
    while i < len(tutors):
        if i < len(klasses):
            yield tuple((tutors[i], klasses[i]))
        else:
            yield tuple((tutors[i], None))
        i += 1
"""



def check_gen(tutors: list, klasses: list):
   return ((tutors[i], klasses[i]) if i < len(klasses) else (tutors[i], None) for i in range(len(tutors)))



tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Слава', "Николай"]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

generator = check_gen(tutors, klasses)
print (type(generator))    # добавьте здесь доказательство, что создали именно генератор
for _ in range(len(tutors)):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration


