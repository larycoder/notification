from application import api
import sql_db as db
from flask import request
from flask import jsonify
from flask_restx import Resource

ns = api.namespace("note", description="Note API")


@ns.route("/api/notes")
class Notes(Resource):
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
        return jsonify(note_dict_list), 200

    def post(self):
        note_dict = request.get_json()
        note = db.Note(**note_dict)
        db.db.session.add(note)
        db.db.session.commit()
        note_persist = db.Note.query.filter_by(id=note.id).first()
        return jsonify({"note_id": note_persist.id}), 200

    def delete(self):
        try:
            del_num = db.db.session.query(db.Note).delete()
            db.db.session.commit()
            return jsonify({"del_num": del_num}), 200
        except Exception as e:
            print(f"[DEBUG] error: {e}")
            db.db.session.rollback()
            return "Fail", 500


@ns.route("/api/note/<string:id>")
class Note(Resource):
    def get(self, id):
        note = db.Note.query.filter_by(id=id).first()
        if note is None:
            return "Fail", 404
        return (
            jsonify(
                {
                    "id": note.id,
                    "subject": note.subject,
                    "content": note.content,
                }
            ),
            200,
        )

    def delete(self, id):
        try:
            note = db.Note.query.filter_by(id=id).first()
            if note is None:
                return "Fail", 404
            db.db.session.delete(note)
            db.db.session.commit()
            return jsonify({"del_id": note.id}), 200
        except Exception as e:
            print(f"[DEBUG] error: {e}")
            db.db.session.rollback()
            return "Fail", 500

    def patch(self, id):
        try:
            note = db.Note.query.filter_by(id=id).first()
            if note is None:
                return "Fail", 404
            for k, v in request.get_json().items():
                setattr(note, k, v)
            db.db.session.commit()
            return jsonify({"patched_id": note.id}), 200
        except Exception as e:
            print(f"[DEBUG] error: {e}")
            db.db.session.rollback()
            return "Fail", 500
