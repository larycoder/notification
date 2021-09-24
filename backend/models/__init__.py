# __init__ file of models module
from sqlalchemy.orm import registry
from db.engine import engine


mapped_registry = registry()
Base = mapped_registry.generate_base()


# Register model
from models.NoteModel import NoteModel


# Emit DDL to DB
Base.metadata.create_all(engine)