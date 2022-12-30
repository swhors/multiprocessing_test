from app.service import get_flask
flask_app, flask_db = get_flask()


class User(flask_db.Model):
    __tablename__ = "user"

    _id = flask_db.Column("id", flask_db.BigInteger, primary_key=True, autoincrement=True)
    _name = flask_db.Column("name", flask_db.String(64))
    _region = flask_db.Column("region", flask_db.String(64))
    _status = flask_db.Column("status", flask_db.Boolean)

    def __init__(self, name: str = "", region: str = "ko", status: bool = True):
        self.name = name
        self.region = region
        self.status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val: int):
        self._id = val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val: str):
        self._name = val

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, val: str):
        self._region = val

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, val: bool):
        self._status = val

    def __repr__(self):
        return f'id : {self._id}, name : {self._name}, region : {self._region}, status : {self._status}'

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}