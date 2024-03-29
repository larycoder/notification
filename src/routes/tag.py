from application import api
import sql_db as db
from flask import request
from flask_restx import Resource, fields

tag_ns = api.namespace("tag", description="tag object")
tags_ns = api.namespace("tags", description="tag list object")

tag_model = api.model(
    "Tag",
    {
        "id": fields.Integer,
        "name": fields.String,
        "notes": fields.Integer,
    },
)


@tags_ns.route("")
class Tags(Resource):
    @api.marshal_with(tag_model, as_list=True)
    def get(self):
        tags = db.Tag.query.all()
        tags_list = []
        for tag in tags:
            tags_list.append(
                {
                    "id": tag.id,
                    "name": tag.name,
                }
            )
        return tags_list, 200

    @api.response(500, "Internal error.")
    def delete(self):
        try:
            del_num = db.db.session.query(db.Tag).delete()
            db.db.session.commit()
            return {"del_num": del_num}, 200
        except Exception as e:
            print(f"[DEBUG] error: {e}")
            db.db.session.rollback()
            return "FAIL", 500

    @api.expect(tag_model)
    @api.response(500, "Internal error.")
    def post(self):
        tag_dict = request.get_json()
        tag = db.Tag(**tag_dict)
        db.db.session.add(tag)
        db.db.session.commit()
        tag_persist = db.Tag.query.filter_by(id=tag.id).first()
        return {"tag_id": tag_persist.id}, 200


@tag_ns.route("/<string:id>")
@api.doc(params={"id": "Tag ID"})
class Tag(Resource):
    @api.response(400, "Tag not found.")
    @api.response(500, "Internal error.")
    def get(self, id):
        tag = db.Tag.query.filter_by(id=id).first()
        if tag is None:
            return "Fail", 400
        return {
            "id": tag.id,
            "name": tag.name,
            "notes": [note.id for note in tag.notes],
        }, 200

    @api.response(500, "Internal error.")
    def delete(self, id):
        try:
            tag = db.Tag.query.filter_by(id=id).first()
            if tag is None:
                return "Fail", 404
            db.db.session.delete(tag)
            db.db.session.commit()
            return {"del_id": tag.id}, 200
        except Exception as e:
            print(f"[DEBUG] error: {e}")
            db.db.session.rollback()
            return "Fail", 500
