from sqlalchemy import (
    Column, Integer,
    Text, DateTime
)
from sqlalchemy import func
from sqlalchemy import ForeignKey

from models import BaseModel, ReprModel
from utils.TimeUtil import TimeUtil

class DiaryModel(BaseModel, ReprModel):
    __tablename__ = 'diary'

    id = Column(Integer, primary_key=True, autoincrement=True)
    activity = Column(Text, nullable=False)
    notes = Column(Text, nullable=True)
    created_time = Column(DateTime, server_default=func.now())
    start_time = Column(DateTime, nullable=True)
    duration = Column(Integer, nullable=True)
    taskId = Column(Integer, ForeignKey("tasks.id"))

    @staticmethod
    def __export_attribute():
        attrs = [
            'id', 'activity', 'notes', 'created_time',
            'start_time', 'duration', 'taskId'
        ]
        return attrs[:]

    def toJSON(self) -> dict:
        attribute_list = DiaryModel.__export_attribute()
        json = {}
        for k in attribute_list:
            if k == 'duration':
                json[k] = str(TimeUtil.second_to_datetime(self.duration))
            else:
                json[k] = self.__dict__.get(k)
        return json

    def loadJSON(self, obj: dict):
        attr_list = DiaryModel.__export_attribute()
        attr_list.remove('id')
        for k in attr_list:
            self.__dict__[k] = obj.get(k)