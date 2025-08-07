from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

Database_url = "mysql+mysqldb://root:Root%40123@localhost/practice"

engine = create_engine(Database_url,pool_pre_ping=True)

Sessionlocal = sessionmaker(bind=engine,autocommit =False,autoflush=False)

Base= declarative_base()

# engine =create_engine("mysql+mysqldb://root:Root%40123@localhost/practice")
# connection = engine.connect()
# print("connected")
