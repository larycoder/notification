from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime
)
from sqlalchemy import func
from models import BaseModel, ReprModel


class NoteModel(BaseModel, ReprModel):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    created_time = Column(DateTime, server_default=func.now())
    updated_time = Column(DateTime, server_default=func.now())

    @staticmethod
    def __export_attribute():
        attrs = [
            'id', 'subject', 'content',
            'created_time', 'updated_time'
        ]
        return attrs[:]

    def toJSON(self) -> dict:
        attribute_list = NoteModel.__export_attribute()
        json = {}
        for k in attribute_list:
            json[k] = self.__dict__.get(k)
        return json

    def loadJSON(self, obj: dict):
        attr_list = NoteModel.__export_attribute()
        attr_list.remove('id')
        for k in attr_list:
            if k in obj.keys():
                setattr(self, k, obj.get(k))