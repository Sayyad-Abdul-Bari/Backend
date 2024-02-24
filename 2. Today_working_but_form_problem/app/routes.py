from flask import request, jsonify
from app import app, db
from app.models import CardStatus

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
        return jsonify({"error": "Card not found"}), 404

    return jsonify(card_status.as_dict())
