from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'
    id            = Column(Integer, primary_key=True)
    title         = Column(String)
    category      = Column(String)
    
    def __init__(self, title, category):
        self.title = title
        self.category = category



