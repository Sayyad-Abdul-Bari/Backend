from app import app
from app.services import create_all_tables, populate_tables
from flask import Flask

# set the template folder
app = Flask(__name__, template_folder='templates')

if __name__ == "__main__":
    create_all_tables()  # Create tables if not already existing
    populate_tables()  # Populate tables with data (optional, uncomment if needed)

    app.run(host="0.0.0.0",debug=True)
