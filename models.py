from sqlalchemy import create_engine, func
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Audio_Engineer(Base):
   __tablename__ = 'audio_engineers'

   id = Column(Integer(), primary_key=True)
   name = Column(String())
   created_at = Column(DateTime(), server_default=func.now())
   updated_at = Column(DateTime(), onupdate=func.now())

   def __repr__(self):
       return f'Audio_Engineer(id={self.id}, name="{self.name}")'

if   __name__ == '__main__':
		engine = create_engine('sqlite:///audio_engineers.db')
		Base.metadata.create_all(engine)



