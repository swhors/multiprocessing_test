class MysqlConfig:
    def __init__(self, host: str = "127.0.0.1", port: int = 3306, user: str = "tester", password: str = "tester", database: str = "test"):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database = database

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def user(self):
        return self._user

    @property
    def passwd(self):
        return self._passwd

    @property
    def database(self):
        return self._database

    @property
    def config(self):
        return {
            'user': self._user,
            'password': self._password,
            'host': self._host,
            'port': self._port,
            'database': self._database
        }

    @property
    def db_url(self):
        return f"mysql+pymysql://{self._user}:{self._password}@{self._host}:{self._port}/{self._database}"


class PoolConfig:
    def __init__(self):
        self._size = 5
        self._is_async = True

    @property
    def size(self):
        return self._size

    @property
    def is_async(self):
        return self._is_async


class Config:
    def __init__(self):
        self._mysql: MysqlConfig = MysqlConfig()
        self._pool: PoolConfig = PoolConfig()

    @property
    def mysql(self):
        return self._mysql

    @property
    def pool(self):
        return self._pool


class TestConfig(Config):
    def __init__(self):
        super().__init__()


current_config = TestConfig()

if __name__ == "__main__":

    print(f"{current_config}, {current_config.pool.size}")
