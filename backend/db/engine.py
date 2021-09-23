from sqlalchemy import create_engine


# sqlite engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)