from application import api
import sql_db as db
from flask import request
from flask_restx import Resource

# tag_ns = api.namespace("Tag", description="tag object")
tags_ns = api.namespace("Tags", description="tag list object")


@tags_ns.route("")
class Tags(Resource):
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

    def delete(self):
        try:
            del_num = db.db.session.query(db.Tag).delete()
            db.db.session.commit()
            return {"del_num": del_num}, 200
        except Exception as e:
            print(f"[DEBUG] error: {e}")
            db.db.session.rollback()
            return "FAIL", 500

    def post(self):
        tag_dict = request.get_json()
        tag = db.Tag(**tag_dict)
        db.db.session.add(tag)
        db.db.session.commit()
        tag_persist = db.Tag.query.filter_by(id=tag.id).first()
        return {"tag_id": tag_persist.id}, 200


# @tag_ns.route("/<string:id>")
# class Tag(Resource):
#    pass
