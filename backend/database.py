from sqlalchemy import Column, Integer, String, create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

DATABASE_URL = "mysql+mysqlconnector://root:mysql@localhost/usermanagement_fastapi"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())


class UserModel(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    username = Column(String(30), unique=True)
    email = Column(String(30))
    phone = Column(String(10))
    password = Column(String(30))

Base.metadata.create_all(bind=engine)


