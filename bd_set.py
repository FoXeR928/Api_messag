from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from config import base_ip, base_port, base_name, base_user, base_passw, table_users,table_message

Base = declarative_base()
engine = create_engine(f"postgres://{base_ip}:{base_port}@{base_user}:{base_passw}/{base_name}")

Base.metadata.create_all(engine)

class USERS(Base):
    __tablename__ = table_users
    id=Column(Integer, primary_key=True, unique=True)
    user=Column(String, primary_key=True)
    ip=Column(String)

class MESSAGE(Base):
    __tablename__ = table_message
    id=Column(Integer,primary_key=True, unique=True)
    user=Column(String, ForeignKey("users.user"))
    user_to=Column(String, ForeignKey("users.user"))
    message=Column(String)
    status=Column(Integer, null=False)
