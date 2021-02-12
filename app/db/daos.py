from db.schemas import (
    notes_t,
    relations_t
)


class BaseDAO:
    @staticmethod
    def to_string(data):
        return f'"{data}"'


class NoteDAO(BaseDAO):
    @staticmethod
    def add_note(note_id, note_name, parent_id = None):
        note = notes_t()

        # convert data to string
        note_id = BaseDAO.to_string(note_id)
        note_name = BaseDAO.to_string(note_name)
        if parent_id: parent_id = BaseDAO.to_string(parent_id)

        # add note
        note.note_id = note_id
        note.note_name = note_name
        note.insert_data()

        # add relation
        if parent_id:
            relation = relations_t()
            relation.relation_id = f'{parent_id}_{note_id}'
            relation.parent_id = parent_id
            relation.child_id = note_id
            relation.insert_data()
    
    @staticmethod
    def delete_note(note_id):
        note = notes_t()
        relation = relations_t()

        # convert data to string
        note_id = BaseDAO.to_string(note_id)

        # delete note in note table
        where = [f'{note._note_id} = {note_id}']
        note.delete_data(where)

        # delete note in relation table
        where = [f'{relation._child_id} = {note_id}']
        relation.delete_data(where)