from application import api
import sql_db as db
from flask import request
from flask_restx import Resource, fields

note_ns = api.namespace("note", description="note object")
notes_ns = api.namespace("notes", description="note list object")


note_model = api.model(
    "Note",
    {
        "id": fields.Integer,
        "subject": fields.String,
        "content": fields.String(example="Not existed in list GET response."),
    },
)


@notes_ns.route("")
class Notes(Resource):
    @api.marshal_with(note_model, as_list=True)
    def get(self):
        note_list = db.Note.query.all()
        note_dict_list = []
        for item in note_list:
            note_dict_list.append(
                {
                    "id": item.id,
                    "subject": item.subject,
                }
            )
        return note_dict_list, 200

    @api.expect(note_model)
    def post(self):
        note_dict = request.get_json()
        note = db.Note(**note_dict)
        db.db.session.add(note)
        db.db.session.commit()
        note_persist = db.Note.query.filter_by(id=note.id).first()
        return {"note_id": note_persist.id}, 200

    @api.response(500, "Internal error.")
    def delete(self):
        try:
            del_num = db.db.session.query(db.Note).delete()
            db.db.session.commit()
            return {"del_num": del_num}, 200
        except Exception as e:
            print(f"[DEBUG] error: {e}")
            db.db.session.rollback()
            return "Fail", 500


@note_ns.route("/<string:id>")
@api.doc(params={"id": "Note ID"})
class Note(Resource):
    @api.response(200, "Success.", note_model)
    def get(self, id):
        note = db.Note.query.filter_by(id=id).first()
        if note is None:
            return "Fail", 404
        return {"id": note.id, "subject": note.subject, "content": note.content}, 200

    @api.response(500, "Internal error.")
    def delete(self, id):
        try:
            note = db.Note.query.filter_by(id=id).first()
            if note is None:
                return "Fail", 404
            db.db.session.delete(note)
            db.db.session.commit()
            return {"del_id": note.id}, 200
        except Exception as e:
            print(f"[DEBUG] error: {e}")
            db.db.session.rollback()
            return "Fail", 500

    @api.expect(note_model)
    @api.response(500, "Internal error.")
    def patch(self, id):
        try:
            note = db.Note.query.filter_by(id=id).first()
            if note is None:
                return "Fail", 404
            for k, v in request.get_json().items():
                setattr(note, k, v)
            db.db.session.commit()
            return {"patched_id": note.id}, 200
        except Exception as e:
            print(f"[DEBUG] error: {e}")
            db.db.session.rollback()
            return "Fail", 500
