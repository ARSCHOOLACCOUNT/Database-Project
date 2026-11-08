#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

url = URL.create(
    "mysql+mysqlconnector",
    username=os.getenv("SQL_USER"),
    password=os.getenv("SQL_PWD"),
    host=os.getenv("SQL_HOST"),
    database=os.getenv("SQL_DB")
)
engine = create_engine(url)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Staff(Base):
    __tablename__ = "staff"
    staff_id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    email = Column(String(50))
    username = Column(String(16))
    password = Column(String(40))

def show_staff():
    session = Session()
    results = session.query(Staff).all()
    for s in results:
        print(s.staff_id, s.first_name, s.last_name, s.email, s.username, s.password)
    session.close()

def add_staff():
    fn = input("first name: ")
    ln = input("last name: ")
    em = input("email: ")
    un = input("username: ")
    pw = input("password: ")
    session = Session()
    new_staff = Staff(first_name=fn, last_name=ln, email=em, username=un, password=pw)
    session.add(new_staff)
    session.commit()
    session.close()
    print("added")

def update_staff():
    sid = input("staff id to update: ")
    session = Session()
    s = session.get(Staff, sid)
    if s == None:
        print("no staff with that id")
        session.close()
        return
    print("current:", s.first_name, s.last_name, s.email, s.username, s.password)
    s.first_name = input("new first name: ")
    s.last_name = input("new last name: ")
    s.email = input("new email: ")
    s.username = input("new username: ")
    s.password = input("new password: ")
    session.commit()
    session.close()
    print("updated")

def delete_staff():
    sid = input("staff id to delete: ")
    session = Session()
    s = session.get(Staff, sid)
    if s == None:
        print("no staff with that id")
    else:
        session.delete(s)
        session.commit()
        print("deleted")
    session.close()

menu = """1. display staff (R)
2. insert staff (C)
3. update staff (U)
4. delete staff (D)
q. quit
"""

choice = ""
while choice != "q":
    choice = input(menu)
    if choice == "1":
        show_staff()
    elif choice == "2":
        add_staff()
    elif choice == "3":
        update_staff()
    elif choice == "4":
        delete_staff()