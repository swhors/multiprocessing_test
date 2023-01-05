import multiprocessing as mp
import multiprocessing.dummy as th
import time
from app.config import current_config
from itertools import product


def wrapped_timer(func):
    def inner(*args):
        start_ts: time.time = time.time()
        result = func(*args)
        end_ts: time.time = time.time()
        print(f"{func.__name__} elapsed = {end_ts - start_ts}")
        return result

    return inner


class ExtInfo:
    ext_num: int

    def __init__(self):
        self.ext_num = 10


def f(ext_info, num):
    # time.sleep(1)
    result = num * num * ext_info.ext_num
    # print(f'{num} * {num} * {ext_info.ext_num} = {result}')
    return result


@wrapped_timer
def test_multi_process():
    ext_info = [ExtInfo(), ]
    with mp.Pool(current_config.pool.size) as p:
        p.starmap(f, product(ext_info, range(1, 31, 1)))


@wrapped_timer
def test_multi_thread():
    ext_info = [ExtInfo(), ]
    with th.Pool(current_config.pool.size) as p:
        p.starmap(f, product(ext_info, range(1, 31, 1)))


@wrapped_timer
def test_single():
    ext_info = ExtInfo()
    for num in range(1, 31, 1):
        f(ext_info, num)


def update_count(user):
    from app.service.goods import ServiceGoods
    ServiceGoods.dec_count_by_ownerid(user.id)


@wrapped_timer
def test_1_multi_process():
    mp.set_start_method("fork")
    from app.service.user import ServiceUser
    users = ServiceUser.get_all()

    with mp.Pool(processes=current_config.pool.size) as p:
        from app.service.goods import dec_count_by_user_with_mp
        if current_config.pool.is_async:
            results = p.map_async(dec_count_by_user_with_mp, users)
            results.wait()
        else:
            p.map(dec_count_by_user_with_mp, users)
        p.terminate()


@wrapped_timer
def test_1_multi_thread():
    from app.service.user import ServiceUser
    users = ServiceUser.get_all()

    with th.Pool(current_config.pool.size) as p:
        from app.service.goods import dec_count_by_user_with_mp
        if current_config.pool.is_async:
            results = p.map_async(dec_count_by_user_with_mp, users)
            results.wait()

        else:
            p.map(dec_count_by_user_with_mp, users)
        p.terminate()


@wrapped_timer
def test_1_single():
    from app.service.user import ServiceUser
    from app.service.goods import ServiceGoods
    users = ServiceUser.get_all()
    for user in users:
        ServiceGoods.dec_count_by_user(user)


test_subcmd = {"simple": [test_multi_process, test_1_multi_thread, test_single], "data": [test_1_multi_process, test_1_multi_thread, test_1_single]}


def test_data(*args):
    for func in args[0]:
        func()
