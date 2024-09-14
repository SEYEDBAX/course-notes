from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

from db import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="orders")


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)