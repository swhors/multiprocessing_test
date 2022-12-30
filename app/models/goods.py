from app.service import get_flask

flask_app, flask_db = get_flask()


class Goods(flask_db.Model):
    __tablename__ = "goods"

    _id = flask_db.Column('id', flask_db.BigInteger, primary_key=True, autoincrement=True)
    _name = flask_db.Column('name', flask_db.String(64))
    _owner = flask_db.Column('owner', flask_db.String(64))
    _price = flask_db.Column('price', flask_db.Integer)
    _count = flask_db.Column('count', flask_db.Integer)
    _owner_id = flask_db.Column('owner_id', flask_db.BigInteger)

    def __init__(self, name: str, owner: str, price: int, count: int, owner_id: int):
        self._name = name
        self._owner = owner
        self._price = price
        self._owner_id = owner_id
        self._count = count

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val: str):
        self._name = val

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, val: str):
        self._owner = val

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val: int):
        self._price = val

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, val: int):
        self._count = val

    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, val: int):
        self._owner_id = val

    def __repr__(self):
        return f'id : {self._id}, name : {self._name}, owner : {self._owner}, price : {self._price}, count : {self._count}, owner_id : {self._owner_id}'

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}
