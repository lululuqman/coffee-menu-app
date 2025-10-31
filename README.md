☕ Coffee Menu App

A simple Full-Stack Coffee Menu application built with FastAPI, PostgreSQL, and Streamlit.
You can view, add, edit, and delete coffee items — all from an easy visual interface.

🧰 Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI (Uvicorn)
Database	PostgreSQL (via SQLAlchemy)
Tools	pgAdmin, Python, VS Code
📂 Project Structure
coffee-menu-app/
│
├── backend/
│   ├── main.py              # FastAPI app (API endpoints)
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── database.py          # Database connection (PostgreSQL)
│   ├── requirements.txt     # Backend dependencies
│
├── frontend/
│   ├── app.py               # Streamlit app UI
│   ├── requirements.txt     # Frontend dependencies
│
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/coffee-menu-app.git
cd coffee-menu-app

2️⃣ Backend Setup

Open the backend folder in VS Code.

Create a virtual environment:

python -m venv .venv
.venv\Scripts\activate   # on Windows


Install dependencies:

pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic


Configure your database in backend/database.py:

DATABASE_URL = "postgresql://your_user:your_password@localhost:5432/coffee_menu"


You can check or create this database in pgAdmin.

Run the backend:

uvicorn backend.main:app --reload


Visit: http://127.0.0.1:8000/docs

3️⃣ Frontend Setup

Open another terminal.

Go to the frontend folder:

cd frontend


Create another virtual environment:

python -m venv .venv
.venv\Scripts\activate


Install dependencies:

pip install streamlit requests


Run the Streamlit app:

streamlit run app.py


Visit: http://localhost:8501

🎯 Features

View coffee menu (sorted by price)

Add new coffee items

Edit existing coffee info

Delete coffee items

Persistent PostgreSQL database
