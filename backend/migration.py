from db.engine import engine
from models import BaseModel
from models.NoteModel import NoteModel
from models.TaskModel import TaskModel


if __name__ == '__main__':
    BaseModel.metadata.create_all(engine)