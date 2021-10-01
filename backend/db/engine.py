from sqlalchemy import create_engine


# sqlite engine
sql_connection = "mysql://username:password@127.0.0.1:3306/notification"
engine = create_engine(sql_connection, echo=True, future=True)