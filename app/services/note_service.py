from db.schemas import notes_t
from utils.common_util import DataUtil

import json


class NoteService:
    @staticmethod
    def get_note_list(column):
        note = notes_t()

        # retrieve data
        data = [c for c in note.get_column(column)]
        schema = note._fields_name

        data_list = DataUtil.convert_data_to_dict(schema, data)

        return {'data': data_list}
