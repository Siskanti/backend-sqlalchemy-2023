from sqlalchemy.orm  import sessionmaker, declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/toko"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    echo=True
)

sessionLoc = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
   
    try:
        db = sessionLoc()
        yield db
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()