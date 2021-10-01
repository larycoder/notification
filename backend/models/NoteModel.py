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

    def toJSON(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'content': self.content,
            'created_time': self.created_time,
            'updated_time': self.updated_time
        }