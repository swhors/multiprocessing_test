import multiprocessing as mp
import time
# import os
from app.config import current_config
from itertools import product


class ExtInfo:
    ext_num: int

    def __init__(self):
        self.ext_num = 10


def f(num, ext_info):
    # print(f'{os.getpid()}/{os.getppid()}')
    time.sleep(1)
    result = num * num * ext_info.ext_num
    print(f'{num} * {num} * {ext_info.ext_num} = {result}')
    return result


def test_multi():
    ext_info = [ExtInfo(),]
    start_ts: time.time = time.time()
    with mp.Pool(current_config.pool.size) as p:
        p.starmap(f, product(range(1, 31, 1), ext_info))
    end_ts: time.time = time.time()

    print(f"multi op wrapped = {end_ts - start_ts}")


def test_single():
    ext_info = ExtInfo()
    start_ts: time.time = time.time()
    for num in range(1, 31, 1):
        f(num, ext_info)
    end_ts: time.time = time.time()
    print(f"sequential op wrapped = {end_ts - start_ts}")


def update_count(user):
    from app.service.goods import ServiceGoods
    ServiceGoods.dec_count_by_ownerid(user.id)


def test_1_multi():
    mp.set_start_method("fork")
    start_ts: time.time = time.time()
    from app.service.user import ServiceUser
    users = ServiceUser.get_all()

    with mp.Pool(current_config.pool.size) as p:
        from app.service.goods import dec_count_by_user_with_mp
        p.map(dec_count_by_user_with_mp, users)
    end_ts: time.time = time.time()
    print(f"multi op wrapped = {end_ts - start_ts}")


def test_1_single():
    start_ts: time.time = time.time()
    from app.service.user import ServiceUser
    from app.service.goods import ServiceGoods
    users = ServiceUser.get_all()
    for user in users:
        ServiceGoods.dec_count_by_user(user)
    end_ts: time.time = time.time()
    print(f"sequential op wrapped = {end_ts - start_ts}")


test_subcmd = {"simple": [test_multi, test_single], "data": [test_1_multi, test_1_single]}


def test_data(*args):
    for func in args[0]:
        func()
