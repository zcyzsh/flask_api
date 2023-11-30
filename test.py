from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


HOST_NAME = '127.0.0.1'	# 主机
PORT = '3306'	# 端口号
DB_NAME = 'test_db'
USERNAME = 'root'
PASSWORD = '123456'

DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOST_NAME, PORT, DB_NAME
)
engine = create_engine(DB_URL)

Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'	# 数据库中的表名
    id = Column(Integer, primary_key=True, autoincrement=True)	# 主键
    name = Column(String(50), unique=True, nullable=False)
    password = Column(String(50))
    create_time = Column(DateTime, default=datetime.now())

if __name__ == '__main__':
    # 创建表
    Base.metadata.create_all()