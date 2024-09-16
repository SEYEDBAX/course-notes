from sqlalchemy import Column, Integer, String, ForeignKey, Table

from sqlalchemy.orm import relationship

from db import Base

# جدول میانی بین User و Book
user_books = Table('user_books', Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('book_id', ForeignKey('books.id'), primary_key=True)
)


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    orders = relationship("Order", back_populates="user")
    books = relationship("Book", secondary=user_books, back_populates="users")


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="orders")


class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)

    users = relationship("User", secondary=user_books, back_populates="books")