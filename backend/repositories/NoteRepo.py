from sqlalchemy import text
from repositories import BaseRepo
from models.NoteModel import NoteModel


class NoteRepo(BaseRepo):
    def __init__(self):
        super().__init__(NoteModel)

    def main(self):
        insert_list = [
            self.insert(subject="[FIRST]", content="Hello World"),
            self.insert(subject="[SECOND]", content="Nice to meet you"),
        ]
        self.execute_many(insert_list)

        result = self.execute(self.select())
        for row in result:
            print(row)


if __name__ == '__main__':
    note = NoteRepo()
    note.main()