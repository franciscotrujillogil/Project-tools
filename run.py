# --- 4. run.py (Application Entry Point) ---
# This file is the primary script used to run your Flask application.

# run.py
import os
from dotenv import load_dotenv # Used to load environment variables from .flaskenv and .env

# Load environment variables from .env and .flaskenv files.
# .env typically holds sensitive data (SECRET_KEY, DB credentials).
# .flaskenv typically holds Flask-specific variables (FLASK_APP, FLASK_ENV).
# load_dotenv() loads them from both if they exist in the current directory.
load_dotenv()

# Import the application factory and database instance from your package
from flask_app import create_app, db

# Determine the configuration environment.
# FLASK_ENV (from .flaskenv or OS env) is typically 'development' or 'production'.
# This directly maps to the config class we want to load.
config_name = os.environ.get('FLASK_ENV', 'development') # Default to 'development'

# Create the Flask application instance using the factory function
app = create_app(config_name)

# Ensure database tables are created within the application context.
# In production, use database migration tools (like Flask-Migrate/Alembic)
# instead of db.create_all() for managing schema changes.
with app.app_context():
    db.create_all()

# Run the application.
# app.config['DEBUG'] will be True for development, False for production.
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
