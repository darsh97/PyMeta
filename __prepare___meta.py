from itertools import count


class CustomDict(dict):
    def __init__(self):
        self.int_cnt = count()
        super().__init__()

    def __getitem__(self, item):
        if str(item).split('_')[0] == 'int':
            self[item] = next(self.int_cnt)
        else:
            super().__getitem__(item)


class Meta(type):
    def __new__(mcs, cls_name, bases, cls_body):
        _instance = super().__new__(mcs, cls_name, bases, cls_body)
        return _instance

    @classmethod
    def __prepare__(mcs, name, bases):
        return CustomDict()


class Foo(metaclass=Meta):
    int_A
    int_B
    int_C


foo = Foo()
print(Foo.int_A)  # 0
print(Foo.int_B)  # 1
print(Foo.int_C)  # 2
