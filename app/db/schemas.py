from db.engines import sqlite_engine
import re


class base_t:
    def __init__(self):
        self.__table__  = None
        self.init_schema()
        self.engine = sqlite_engine

    def init_schema(self): # used to init table and fields name
        pass

    def query_beautify(self, query):
        return re.sub(' +', ' ', query.replace('\n', ' ').strip())

    def get_execute(self, query):
        query = self.query_beautify(query)
        return self.engine.execute(query)

    def commit_execute(self, query):
        query = self.query_beautify(query)
        self.engine.execute(query)
        self.engine.commit()

    def get_column(self, column, where:list = []):
        where = ' AND '.join(['1=1'] + where)
        query = f'''
            SELECT {column} 
            FROM {self.__table__}
            WHERE {where}
        '''
        return self.get_execute(query)

    def get_list(self):
        '''
            inherited function use to pass value to insert function
            @return fields, values
        '''
        return [], []

    def insert_data(self):
        fields, values = self.get_list()

        # clean data before insert
        fields = [fields[i] for i, v in enumerate(values) if v]
        values = [v for v in values if v]

        # build query
        fields = ','.join(fields)
        values = ','.join(values)
        query = f'''
            INSERT INTO {self.__table__} ({fields}) VALUES ({values})
        '''
        self.commit_execute(query)

    def delete_data(self, where:list = None):
        where = ' AND '.join(['1=1'] + where)
        query = f'''
            DELETE FROM {self.__table__}
            WHERE {where}
        '''
        self.commit_execute(query)


class notes_t(base_t):
    def init_schema(self):
        self.__table__ = 'NOTES_T'
        self._fields_name = ['note_id', 'note_name']

        # field value
        self.note_id = None
        self.note_name = None

    def get_list(self):
        value_list = [self.note_id, self.note_name]
        return self._fields_name, value_list


class relations_t(base_t):
    def init_schema(self):
        self.__table__ = 'RELATIONS_T'
        self._fields_name = ['parent_id', 'child_id']

        # field value
        self.parent_id = None
        self.child_id = None

    def get_list(self):
        value_list = [self.parent_id, self.child_id]
        return self._fields_name, value_list


class tables_t(base_t):
    def init_schema(self):
        self.__table__ = 'TABLES_T'
        self._fields_name = ['table_id', 'table_name', 'note_id']

        # field value
        self.table_id = None
        self.table_name = None
        self.note_id = None

    def get_list(self):
        value_list = [self.table_id, self.table_name, self.note_id]
        return self._fields_name, value_list


class cells_t(base_t):
    def init_schema(self):
        self.__table__ = 'CELLS_T'
        self._fields_name = [
            'cell_id', 'table_id', 'cell_name', 'cell_note',
            'start_time', 'end_time', 'is_notify'
        ]

        # field value
        self.cell_id = None
        self.table_id = None
        self.cell_name = None
        self.cell_note = None
        self.start_time = None
        self.end_time = None
        self.is_notify = None

    def get_list(self):
        value_list = [
            self.cell_id, self.table_id, self.cell_name,
            self.cell_note, self.start_time, self.end_time,
            self.is_notify
        ]
        return self._fields_name, value_list