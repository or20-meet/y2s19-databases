from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name, topic, rating):
	knowledge_object=  Knowledge(name=name ,topic=topic, rating=rating )
	session.add(knowledge_object)
	session.commit()
	

def query_all_articles():
	k=session.query(Knowledge).all()
	return k

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass

add_article("idk", "something", 3)
add_article("hello", "greetings", 7)
print(query_all_articles())


