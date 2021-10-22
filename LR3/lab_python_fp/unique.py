# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = False, Aбв и АБВ - разные строки
        #           ignore_case = True, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.case_sens = kwargs.get('ignore_case')
        self.set = set()
        self.items = iter(items)

    def __next__(self):
        # Нужно реализовать __next__
        a = next(self.items)
        if self.case_sens:
            if a.lower() not in self.set:
                self.set.add(a.lower())
            else:
                a = self.__next__()
        else:
            if a not in self.set:
                self.set.add(a)
            else:
                a = self.__next__()
        return a

    def __iter__(self):
        return self

