from datetime import datetime
def timeit(func):
    def wrapper(val):
        start = datetime.now()
        res = func(val)
        end = datetime.now()
        print(f"time: {end-start}")
        return res
    return wrapper

@timeit
def get_list_1(val):
    return [i for i in range(val) if i %2]

@timeit
def get_list_2(val):
    n_list = []
    for i in range(val):
        if i%2:
            n_list.append(i)
    return n_list

print(get_list_1(10000000) == get_list_2(10000000))