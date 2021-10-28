from db.engine import engine
from models import BaseModel
from models.NoteModel import NoteModel
from models.TaskModel import TaskModel
from models.DiaryModel import DiaryModel


if __name__ == '__main__':
    BaseModel.metadata.create_all(engine)