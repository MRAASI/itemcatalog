import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    picture = Column(String(300))


class LanguageName(Base):
    __tablename__ = 'languagename'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="languagename")

    @property
    def serialize(self):
        """Return objects data in easily serializeable formats"""
        return {
            'name': self.name,
            'id': self.id
        }


class PaperName(Base):
    __tablename__ = 'papername'
    id = Column(Integer, primary_key=True)
    name = Column(String(350), nullable=False)
    year = Column(String(150))
    
    price = Column(String(10))
    rating = Column(String(250))
    
    languagenameid = Column(Integer, ForeignKey('languagename.id'))
    languagename = relationship(
        LanguageName, backref=backref('papername', cascade='all, delete'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="papername")

    @property
    def serialize(self):
        """Return objects data in easily serializeable formats"""
        return {
            'name': self. name,
            'year': self. year,
            
            'price': self. price,
            'rating': self. rating,
           
            'id': self. id
        }

engin = create_engine('sqlite:///newspapers.db')
Base.metadata.create_all(engin)
