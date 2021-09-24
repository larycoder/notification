from models.NoteModel import NoteModel
from repositories import BaseRepo


class NoteRepo(BaseRepo):
    def __init__(self):
        super().__init__(NoteModel)
