from db.schemas import (
    notes_t,
    relations_t
)
from utils.common_util import DataUtil

import json


class NoteService:
    @staticmethod
    def get_note_list(column):
        note = notes_t()

        # retrieve data
        data = [r for r in note.get_column(column)]
        schema = note._fields_name

        data_list = DataUtil.convert_data_to_dict(schema, data)
        return {'data': data_list}

    @staticmethod
    def get_note_child(note_id):
        relation = relations_t()

        # retrieve data
        where = [f'{relation._parent_id} = "{note_id}"']
        cursor = relation.get_column('*', where = where)
        data = [r for r in cursor]
        schema = relation._fields_name

        data_list = DataUtil.convert_data_to_dict(schema, data)
        return {'data': data_list}


