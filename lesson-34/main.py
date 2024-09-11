from sqlalchemy.orm import sessionmaker
from models import User
from db import engine, Base

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

def get_users(session):
    users = session.query(User).all()
    for user in users:
        print('username:', user.name, 'age:', user.age)

def input_user():
    name = input("Enter name: ")
    age = input("Enter age: ")
    return User(name=name, age=age)


def add_user(session, user):
    session.add(user)
    session.commit()
    print("User created successfully!")

def search_user(session, name):
    user = session.query(User).filter(User.name.like(f"%{name}%")).first()
    if user:
        print('username:', user.name, '| age:', user.age)
    else:
        print("User not found")


def menu():
    while True:
        print("1. Get users")
        print("2. Add user")
        print("3. Search user")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            get_users(session)
        elif choice == "2":
            user = input_user()
            add_user(session, user)
        elif choice == "3":
            name = input("Enter name: ")
            search_user(session, name)
        elif choice == "4":
            break


if __name__ == "__main__":
    menu()