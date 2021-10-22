# Здесь должна быть реализация декоратора


def print_result(myfunc):
    def wrapper(arg):
        print(myfunc.__name__)
        res = myfunc(arg)
        if type(res) == dict:
            for i in res:
                print('{} = {}'.format(i, res[i]))
        elif type(res) == list:
            for i in res:
                print(i)
        else:
            print(res)
        return res
    return wrapper



@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
        print('!!!!!!!!')
        test_1()
        test_2()
        test_3()
        test_4()