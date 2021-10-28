from models.TaskModel import TaskModel
from repositories import BaseRepo


class TaskRepo(BaseRepo):
    def __init__(self):
        super().__init__(TaskModel)

    def list_all(self):
        stmt = self.select()
        result = self.execute(stmt)
        list_obj = []
        for row in result:
            list_obj.append(row[0])
        return list_obj
