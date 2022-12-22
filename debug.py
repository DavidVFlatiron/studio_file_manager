from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Audio_Engineer

if __name__ == '__main__':
	engine = create_engine('sqlite:///audio_engineers.db')
	Session  = sessionmaker(bind=engine)
	session = Session()
   	import ipdb; ipdb.set_trace()
