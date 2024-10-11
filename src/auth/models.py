from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    Session as SessionType, Session
)

DB_URL = "postgresql://thfmayiq:zRy6wxqO8GU7ONN25dmufYGUj8dPfp-S@raja.db.elephantsql.com:5432/thfmayiq"
DB_ECHO = False
engine = create_engine(url=DB_URL, echo=DB_ECHO)


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(256), nullable=False)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, email={self.email}, username={self.username})"
        )

    def __repr__(self):
        return str(self)


def create_table():
    Base.metadata.create_all(bind=engine)


def main():
    create_table()

if __name__ == '__main__':
    main()