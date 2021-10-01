from db.engine import engine
from models import BaseModel
from models.NoteModel import NoteModel


if __name__ == '__main__':
    BaseModel.metadata.create_all(engine)