from app.service import get_flask, enter_flask_sqlalchemy, enter_flask_sqlalchemy_no_commit
from app.models.goods import Goods

flask_app, flask_db = get_flask()


class ServiceGoods:

    @classmethod
    @enter_flask_sqlalchemy
    def insert(cls, name: str, owner: str, price: int, count: int, owner_id: int):
        goods = Goods(name=name, owner=owner, price=price, count=count, owner_id=owner_id)
        flask_db.session.add(goods)

    @classmethod
    @enter_flask_sqlalchemy
    def delete_all(cls, owner: str = None) -> int:
        if owner is None:
            num_deleted_rows = Goods.query.delete()
        else:
            goods = Goods.query.filter_by(_owner=owner).all()
            num_deleted_rows = flask_db.session.delete(goods)
        return num_deleted_rows

    @classmethod
    @enter_flask_sqlalchemy_no_commit
    def get_all(cls) -> []:
        goods = Goods.query.all()
        return goods

    @classmethod
    @enter_flask_sqlalchemy
    def dec_count_by_ownerid(cls, ownerid: int):
        goods_all = Goods.query.filter_by(_owner_id=ownerid).limit(20).all()
        for goods in goods_all:
            goods.count = goods.count - (1 if goods.count > 0 else 0)

    @classmethod
    def dec_count_by_user(cls, user):
        flask_app.app_context().push()
        goods_all = Goods.query.filter_by(_owner_id=user.id).limit(20).all()
        for goods in goods_all:
            goods.count = goods.count - (1 if goods.count > 0 else 0)

        flask_db.session.commit()
