from model import Base, Post
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

new_post = Post(title ="Title for Post1", category = "Food", debate="This is the Debate for Post1", nickname="Nickname for Post1", comments = [new_comment])

session.add(new_post)
session.commit()
post = session.query(Post).all()