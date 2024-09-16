from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import Book, Order, User
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

def search_user(session, name, as_object=False):
    user = session.query(User).filter(User.name.like(f"%{name}%")).first()
    if user:
        print('username:', user.name, '| age:', user.age)
    else:
        print("User not found")
    
    if as_object:
        return user

def create_order(user):
    if user:
        description = input("Enter description: ")
        order = Order(description=description, user=user)
        session.add(order)
        session.commit()
        print("Order created successfully!")
    else:
        print("User not found")

def avg_users_age():
    average_age = session.query(func.avg(User.age)).scalar()
    print(f"Average age: {average_age}")


def add_book_to_user(session, user):
    book = input("Enter book name: ")
    user.books.append(Book(title=book))
    session.commit()

def menu():
    while True:
        print("1. Get users")
        print("2. Add user")
        print("3. Search user")
        print("4. Exit")
        print("5. Create order")
        print("6. Average users age")
        print("7. Add book to user")
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
        elif choice == "5":
            name = input("Enter name: ")
            user = search_user(session, name, as_object=True)
            print(user)
            create_order(user)
        elif choice == "6":
            avg_users_age()
        elif choice == "7":
            name = input("Enter name: ")
            user = search_user(session, name, as_object=True)
            add_book_to_user(session, user)



if __name__ == "__main__":
    menu()