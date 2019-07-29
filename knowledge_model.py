from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__="Knowledge"
	primary_key= Column(Integer,primary_key=True)
	name= Column(String)
	topic=  Column(String)
	rating= Column(String)
	# Create a table with 4 Columns
	# The first Column will be the primary key
	# The second Column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third Column wSBill be a string representing the 
	# topic of the article. The last Column will be
	# an integer, representing your rating of the article.
	def __repr__(self):
		return("if you want to learn about {}\n, you should look at the wikipedia article called {}\n . We gav e this article a rating of {}\n out of 10").format(self.topic, self.name, self.rating)
