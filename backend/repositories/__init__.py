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

    # Core expression
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

    # ORM expression
    def check_object(self, model):
        if isinstance(model, type(self.model)):
            self.session.close()
            raise Exception('Wrong Model: expecting {type(self.model)} received {type(model)}')

    def add_object(self, model):
        self.check_object(model)
        self.session.add(model)

    def delete_object(self, model):
        self.check_object(model)
        self.session.delete(model)

    def flush(self):
        return self.session.flush()

    def commit(self):
        self.flush()
        return self.session.commit()

    def rollback(self):
        self.flush()
        return self.session.rollback()
