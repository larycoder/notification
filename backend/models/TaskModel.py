from sqlalchemy import (
    Column,
    Integer,
    Float,
    Text,
    DateTime
)
from sqlalchemy import func, ForeignKey
from models import BaseModel, ReprModel


class TaskModel(BaseModel, ReprModel):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    parentId = Column(Integer, ForeignKey("tasks.id"))
    task = Column(Text, nullable=False)
    notes = Column(Text, nullable=True)
    label = Column(Text, nullable=True)
    priority = Column(Text, nullable=True)
    created_time = Column(DateTime, server_default=func.now())
    deadline = Column(DateTime, nullable=True)
    measurement = Column(Text, nullable=True)
    process = Column(Float, nullable=True)

    @staticmethod
    def __export_attribute():
        attrs = [
            'id', 'task', 'notes', 'label', 'priority', 'parentId',
            'created_time', 'deadline', 'measurement', 'process'
        ]
        return attrs[:]

    def toJSON(self) -> dict:
        attribute_list = TaskModel.__export_attribute()
        json = {}
        for k in attribute_list:
            json[k] = self.__dict__.get(k)
        return json

    def loadJSON(self, obj: dict):
        attr_list = TaskModel.__export_attribute()
        attr_list.remove('id')
        for k in attr_list:
            self.__dict__[k] = obj.get(k)