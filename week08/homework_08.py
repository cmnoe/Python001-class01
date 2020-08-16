# 作业一
# 容器序列：list, tuple, collections.deque, dict
# 扁平序列：str
# 可变序列：list, dict, collections.deque
# 不可变序列：tuple, str

# 作业二


def fake_map(func, *args):
    for arg in zip(*args):
        yield func(*arg)


def add(x, y):
    return x + y


iter1 = fake_map(add, [1, 2, 3], [4, 5, 6])
iter2 = map(add,  [1, 2, 3], [4, 5, 6])
print(list(iter1), list(iter2))

# 作业三
import time


def timer(func):
    def decorate(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        print(f'total {time.time() - start_time}')
        return ret

    return decorate


@timer
def test(x, y):
    for i in range(1, 10000):
        x += i * y
    return x


test(8, 6)
