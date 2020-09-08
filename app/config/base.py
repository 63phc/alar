import os

SECRET_KEY = os.getenv("SECRET_KEY") or "supersecterkey"

# Database settings
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Flask settings
DEBUG = True
TESTING = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
