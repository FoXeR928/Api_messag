from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import base_name
from bd_set import Base, engine, USERS, MESSAGE

def open_base(base):
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

def add_message(user, user_to, ip, message):
    session=open_base(base)
    check=session.query(USERS).filter(USERS.user==user).all()
    if len(check)>0:
        point1=USERS(user=user, ip=ip)
        point2=MESSAGE(user=user, user_to=user_to, message=message, status='0')
        session.add(point1,point2)
    else:
        point1=MESSAGE(user=user, user_to=user_to, message=message, status='0')
        session.add(point1)
    query_id=session.query(USERS).
    take_id=query_id.id
    session.commit()
    result={"message":take_id}

def add_status(user):
    session=open_base(base)
    result={"message":"Create"}

def get_all_message(user):
    session=open_base(base)
    check=session.query(USERS).filter(USERS.user==user).all()
    return{'message':check.message}