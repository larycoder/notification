from sqlalchemy import text
from db.engine import engine


class NoteRepo():
    def __init__(self):
        self.engine = engine

    def init_table(self):
        with self.engine.begin() as conn:
            conn.execute(
                text("""
                    CREATE TABLE notes(
                        id INT,
                        subject TEXT,
                        content TEXT,
                        created_time TIMESTAMP,
                        updated_time TIMESTAMP
                    )
                """)
            )

            insert_stmt = text("""
                INSERT INTO notes(id, subject, content)
                VALUES (:i, :s, :c)
            """)
            insert1 = insert_stmt.bindparams(i=1, s='INIT NOTES', c='Good day to start')
            insert2 = insert_stmt.bindparams(i=2, s='SECOND NOTES', c='Good day for second')
            conn.execute(insert1)
            conn.execute(insert2)

    def select(self):
        with self.engine.connect() as conn:
            result = conn.execute(text("""
                SELECT * FROM notes
            """))
            result = result.mappings()
            for row in result:
                print(row)

    def main(self):
        self.init_table()
        self.select()


if __name__ == '__main__':
    note = NoteRepo()
    note.main()