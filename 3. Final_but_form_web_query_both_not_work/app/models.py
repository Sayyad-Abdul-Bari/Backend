
from datetime import datetime
from app import db

class CardStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.String(255))
    user_phone = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    comment = db.Column(db.String(255))

    def as_dict(self):
        return {
            "card_id": self.card_id,
            "user_phone": self.user_phone,
            "timestamp": self.timestamp.isoformat(),
            "comment": self.comment,
        }
