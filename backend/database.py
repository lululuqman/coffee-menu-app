from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ Direct PostgreSQL connection (no .env)
# Format: postgresql://username:password@localhost:5432/database_name
DATABASE_URL = "postgresql://postgres:bunkface@localhost:5432/coffee_menu"

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()