######################
# delete operation


def delete_data(*args):
    from app.service.user import ServiceUser
    from app.service.goods import ServiceGoods

    num_deleted_rows = ServiceUser.delete_all()
    print(f'deleted rows count = {num_deleted_rows}')
    num_deleted_rows = ServiceGoods.delete_all()
    print(f'deleted rows count = {num_deleted_rows}')
