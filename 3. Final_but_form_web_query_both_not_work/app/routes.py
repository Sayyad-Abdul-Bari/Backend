# app/routes.py

from flask import request, jsonify, render_template
from app import app, db
from app.models import CardStatus

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_card_status", methods=["GET"])
def get_card_status():
    identifier = request.args.get("identifier")
    identifier_type = request.args.get("identifier_type")

    if not identifier or not identifier_type:
        return jsonify({"error": "Missing required parameters"}), 400

    if identifier_type not in ["user_phone", "card_id"]:
        return jsonify({"error": "Invalid identifier_type"}), 400

    if identifier_type == "user_phone":
        card_status = (
            CardStatus.query.filter_by(user_phone=identifier)
            .order_by(CardStatus.timestamp.desc())
            .first()
        )
    else:
        card_status = (
            CardStatus.query.filter_by(card_id=identifier)
            .order_by(CardStatus.timestamp.desc())
            .first()
        )

    if not card_status:
        if request.accept_mimetypes.accept_json:
            return jsonify({"error": "Card not found"}), 404
        else:
            return render_template("index.html", error="Card not found")

    if request.accept_mimetypes.accept_json:
        return jsonify(card_status.as_dict()), 200
    else:
        return render_template("index.html", card_status=card_status.as_dict())
