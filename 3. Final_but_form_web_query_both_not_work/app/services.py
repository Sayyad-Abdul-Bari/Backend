from app import app, db
import os
import pandas as pd
from app.models import CardStatus, db
import logging


def create_all_tables():
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            logging.error(f"Error creating database tables: {str(e)}")

def populate_tables(data_folder="data"):
    with app.app_context():
        table_count =0
        for filename in os.listdir(data_folder):
            if filename.startswith("Sample Card Status Info -"):
                filepath = os.path.join(data_folder, filename)
                df = pd.read_csv(filepath)
                # print(f"Filename: {filename}")

                # Process CSV data and populate CardStatus table
                for _, row in df.iterrows():
                    
                    if table_count == 0 or table_count == 1:
                        user_phone = row.get("User contact", "")
                        comment = row.get("Comment", "")
                    elif table_count == 2:
                        comment = 'Pickuped'
                        user_phone = row.get("User Mobile", "")
                    elif table_count == 3:
                        comment = 'Returned'
                        user_phone = row.get("User contact", "")
                    # Convert timestamp string to datetime object
                    timestamp = pd.to_datetime(row.get("Timestamp"), errors='coerce')

                    card_status = CardStatus(
                        card_id=row.get('Card ID', ''),
                        user_phone=user_phone,
                        timestamp=timestamp,
                        comment=comment,
                    )
                    db.session.add(card_status)
            table_count += 1

        db.session.commit()

if __name__ == "__main__":
    create_all_tables()
    populate_tables()
