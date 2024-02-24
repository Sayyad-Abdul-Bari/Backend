from app import app
from app.services import create_all_tables, populate_tables

if __name__ == "__main__":
    create_all_tables()  # Create tables if not already existing
    populate_tables()  # Populate tables with data (optional, uncomment if needed)

    app.run(debug=True)
