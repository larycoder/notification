from models.NoteModel import NoteModel
from repositories import BaseRepo


class DemoRepoUsage(BaseRepo):
    def __init__(self):
        super().__init__(NoteModel)

    def print_result(self):
        print(self.execute(self.select()).scalars().all())

    def demo_insert_orm(self):
        n1 = NoteModel()
        n1.subject = "[FIRST]"
        n1.content = "Hello World"
        self.add_object(n1)

        n2 = NoteModel()
        n2.subject = "[SECOND]"
        n2.content = "Nice to meet you"
        self.add_object(n2)

        self.commit()
        self.print_result()

    def demo_insert_core(self):
        insert_list = [
            self.insert(subject="[FIRST]", content="Hello World"),
            self.insert(subject="[SECOND]", content="Nice to meet you")
        ]
        self.execute_many(insert_list)
        self.print_result()

    def demo_update_orm(self):
        n1 = self.execute(self.select().where(NoteModel.id == 1)).scalar_one()

        # before add object
        print("##### Before change #####")
        self.print_result()

        # after add object
        n1.content = "Content modified"
        self.commit()
        print("##### After change #####")
        self.print_result()

        print("##### Note #####")
        print("Object captured by declaration class auto-flush by default after modifying")


if __name__ == '__main__':
    note = DemoRepoUsage()
    note.demo_insert_core()
    note.demo_insert_orm()
    note.demo_update_orm()