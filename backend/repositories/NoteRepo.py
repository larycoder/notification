from sqlalchemy import text
from repositories import BaseRepo
from models.NoteModel import NoteModel


class NoteRepo(BaseRepo):
    def __init__(self):
        super().__init__(NoteModel)

    def main(self):
        n1 = NoteModel()
        n1.subject = "[FIRST]"
        n1.content = "Hello World"
        self.add_object(n1)

        n2 = NoteModel()
        n2.subject = "[SECOND]"
        n2.content = "Nice to meet you"
        self.add_object(n2)

        self.commit()

        print(self.execute(self.select()).scalars().all())


if __name__ == '__main__':
    note = NoteRepo()
    note.main()