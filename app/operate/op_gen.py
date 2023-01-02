import random


def generate_data(*args):
    from app.service.user import ServiceUser
    from app.service.goods import ServiceGoods

    try:
        data_cnt = int(args[1])
    except ValueError:
        data_cnt = 0

    print(f'data_cnt = {data_cnt}')

    for i0 in range(1, data_cnt+1, 1):
        name = f"tester{i0}"
        region = "ko" if i0 % 2 == 1 else "en"
        ServiceUser.insert(name=name, region=region, status=False)
    users = ServiceUser.get_all()

    for user in users:
        print(f'{user}')
        if user is not None:
            rnd_num = int(random.random() * 100) % 10
            for i1 in range(1, (rnd_num % 3) + 2):
                goods_name = f'goods{i1}'
                ServiceGoods.insert(name=goods_name, owner=user.name, price=rnd_num*200, count=i1*rnd_num, owner_id=user.id)
