# __init__ file for repositories module
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from db.engine import engine
from flask import g


class BaseRepo():

    def __init__(self, model):
        self.model = model
        g._sqlite = getattr(g, "_sqlite", Session(engine))
        self.session = g._sqlite

    def insert(self, **kwargs):
        return insert(self.model).values(kwargs)

    def select(self):
        return select(self.model)

    # Core expression
    def execute_many(self, stmt_list: list) -> list:
        db_type = self.session.bind.dialect.name
        result_list = []
        if db_type == "sqlite": # sqlite is always a transaction
            for stmt in stmt_list:
                result = self.session.execute(stmt)
                result_list.append(result)
        else: # need set query on transaction
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
        if not isinstance(model, self.model):
            raise Exception(
                f'Wrong Model: expecting {self.model} received {type(model)}')

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
