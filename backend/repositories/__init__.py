# __init__ file for repositories module
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from db.engine import engine


class BaseRepo():
    def __init__(self, model):
        self.model = model
        self.session = Session(engine)

    def insert(self, **kwargs):
        return insert(self.model).values(kwargs)

    def select(self):
        return select(self.model)

    def execute_many(self, stmt_list: list) -> list:
        result_list = []
        with self.session.begin():
            for stmt in stmt_list:
                result = self.session.execute(stmt)
                result_list.append(result)
        return result_list

    def execute(self, stmt):
        result_list = self.execute_many([stmt])
        return result_list[0]
