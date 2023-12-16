from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from application import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notification.db"
db = SQLAlchemy(app)

note_tag = db.Table(
    "note_tag",
    db.Column("note_id", db.Integer, db.ForeignKey("note.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(500), nullable=False)
    content = db.Column(db.String(5000), nullable=True)
    tags = db.relationship("Tag", secondary=note_tag, backref="note")

    def tags_set(self, tags: list):
        tag_list = []
        for tag_id in tags:
            tag_list.append(Tag.query.filter_by(id=tag_id).first())
        self.tags = tag_list


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    notes = db.relationship("Note", secondary=note_tag, viewonly=True)


def generate_db():
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    print("[Test 1] Generate database...")
    generate_db()
