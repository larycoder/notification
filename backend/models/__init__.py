# __init__ file of models module
from sqlalchemy.orm import registry
from db.engine import engine


mapped_registry = registry()
BaseModel = mapped_registry.generate_base()


# Class provides representation for model
class ReprModel():
    __table__ = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        c_list = self.__table__.columns.keys()
        data_list = {
            k: v for k, v in vars(self).items() if k in c_list
        }
        return f'{self.__tablename__} {data_list}'

# Register model
from models.NoteModel import NoteModel


# Emit DDL to DB
BaseModel.metadata.create_all(engine)