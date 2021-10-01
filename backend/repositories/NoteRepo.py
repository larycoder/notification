from models.NoteModel import NoteModel
from repositories import BaseRepo


class NoteRepo(BaseRepo):
    def __init__(self):
        super().__init__(NoteModel)

    def list_all(self):
        stmt = self.select()
        result = self.execute(stmt)
        list_obj = []
        for row in result:
            list_obj.append(row[0])
        return list_obj
