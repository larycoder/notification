from db.schemas import (
    notes_t,
    relations_t
)
from db.daos import (
    NoteDAO
)
from utils.common_util import (
    DataUtil,
    KeyUtil
)

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
    def get_note_info(note_id):
        # retrieve relation
        relation = relations_t()
        where = [f'{relation._parent_id} = "{note_id}"']
        select = f'''
            {relation._relation_id},
            {relation._child_id}
        '''
        cursor = relation.get_column(select, where = where)
        data = [r for r in cursor]
        schema = [relation._relation_id, relation._child_id]
        relations_data = DataUtil.convert_data_to_dict(schema, data)
        relations_data = relations_data[0] if len(relations_data) > 0 else {}

        # retrieve note info
        note = notes_t()
        where = [f'{note._note_id} = "{note_id}"']
        data = [r for r in note.get_column('*', where)]
        schema = note._fields_name
        notes_data = DataUtil.convert_data_to_dict(schema, data)
        notes_data = notes_data[0] if len(notes_data) > 0 else {}

        return {
            'note': notes_data,
            'relation': relations_data
        }

    @staticmethod
    def add_new_note(note_name, parent_id=None):
        # NOTE: should have exception handler in here

        # create note key
        note_id = KeyUtil.get_key(note_name)
        
        # add note
        NoteDAO.add_note(note_id, note_name, parent_id)

        # retrieve new note
        data = NoteService.get_note_info(note_id)
        data['message'] = 'successfully'
        return data


