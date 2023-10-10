from application import app
import sql_db as db
from flask import request
from flask import jsonify


@app.route("/api/tags", methods=["GET"])
def route_tags_get():
    tags = db.Tag.query.all()
    tags_list = []
    for tag in tags:
        tags_list.append(
            {
                "id": tag.id,
                "name": tag.name,
            }
        )
    return jsonify(tags_list), 200


@app.route("/api/tags", methods=["DELETE"])
def route_tags_del():
    try:
        del_num = db.db.session.query(db.Tag).delete()
        db.db.session.commit()
        return jsonify({"del_num": del_num}), 200
    except Exception as e:
        print(f"[DEBUG] error: {e}")
        db.db.session.rollback()
        return "FAIL", 500


@app.route("/api/tag", methods=["POST"])
def route_tag_add():
    tag_dict = request.get_json()
    tag = db.Tag(**tag_dict)
    db.db.session.add(tag)
    db.db.session.commit()
    tag_persist = db.Tag.query.filter_by(id=tag.id).first()
    return jsonify({"tag_id": tag_persist.id}), 200
