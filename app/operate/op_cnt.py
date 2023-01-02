######################
# delete operation


def count_data(*args):
    from app.service.user import ServiceUser
    from app.service.goods import ServiceGoods

    if args[1] == "None":
        user_prefix = None
    else:
        user_prefix = args[1]

    num_of_all_user = ServiceUser.count(user_prefix)
    print(f'num_of_all_user = {num_of_all_user}')

    if user_prefix is None:
        num_of_all_goods = ServiceGoods.count()
    else:
        ids = ServiceUser.get_id(user_prefix)
        num_of_all_goods = 0
        for id in ids:
            num_of_all_goods += ServiceGoods.count(user_id=id)
    print(f'num_of_all_goods = {num_of_all_goods}')
