from app.service import get_flask, enter_flask_sqlalchemy, enter_flask_sqlalchemy_no_commit
from app.models.user import User

flask_app, flask_db = get_flask()


class ServiceUser:
    @classmethod
    @enter_flask_sqlalchemy
    def insert(cls, name: str, region: str, status: bool) -> User:
        user = User(name=name, region=region, status=status)
        flask_db.session.add(user)
        user = User.query.filter_by(_name=name).first()
        return user

    @classmethod
    @enter_flask_sqlalchemy
    def delete_all(cls) -> int:
        num_deleted_rows = User.query.delete()
        return num_deleted_rows

    @classmethod
    @enter_flask_sqlalchemy_no_commit
    def get_all(cls) -> []:
        users = User.query.all()
        return users

    @classmethod
    @enter_flask_sqlalchemy_no_commit
    def get(cls, name: str) -> []:
        user = User.query.filter_by(_name=name).first()
        return user

    @classmethod
    @enter_flask_sqlalchemy_no_commit
    def count(cls, name: str = None) -> int:
        if name is None or len(name) == 0:
            return User.query.count()
        return User.query.filter(User._name.like('%' + name + '%')).count()

    @classmethod
    @enter_flask_sqlalchemy_no_commit
    def get_id(cls, name: str = None) -> int:
        if name is None or len(name) == 0:
            return [id for id, in (flask_db.session.query(User._id).all())]
            # return User.query("id").all()
        return [id for id, in (flask_db.session.query(User._id).filter(User._name.like('%' + name + '%')).all())]
