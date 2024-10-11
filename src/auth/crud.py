from datetime import datetime
from .models import User
from .schemas import UserBase
from passlib.hash import sha256_crypt, pbkdf2_sha256

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

def hash_password(password):
    return sha256_crypt.hash(password)

def verify_pass(user_pass, hashed_pass):
    return sha256_crypt.verify(user_pass, hashed_pass)