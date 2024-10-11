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


class Measure(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    downloadSpeed = Column(String, nullable=False)
    uploadSpeed = Column(String, nullable=False)
    coordinates = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, username={self.username})"
        )

    def __repr__(self):
        return str(self)


def create_table():
    Base.metadata.create_all(bind=engine)


def main():
    create_table()


if __name__ == '__main__':
    main()
