from sqlalchemy import (
    create_engine
)

from sqlalchemy.orm import (
    Session as SessionType,
    sessionmaker,
    scoped_session,
)

DB_URL = "postgresql://thfmayiq:zRy6wxqO8GU7ONN25dmufYGUj8dPfp-S@raja.db.elephantsql.com:5432/thfmayiq"
DB_ECHO = False
engine = create_engine(url=DB_URL, echo=DB_ECHO)

def init_db():
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    session: SessionType = Session()
    return session