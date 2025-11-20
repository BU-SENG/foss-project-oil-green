# services/auth_service.py

import sqlite3
import streamlit as st

DB_PATH = "database.db"


# -------------------------------------------------------
# Initialize user table
# -------------------------------------------------------
def init_user_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            matric TEXT,
            program TEXT,
            department TEXT,
            phone TEXT,
            gender TEXT,
            dob TEXT,
            hall TEXT,
            guardian_name TEXT,
            guardian_phone TEXT,
            avatar BLOB
        )
    """)
    conn.commit()
    conn.close()

init_user_table()


# -------------------------------------------------------
# Create User (Signup)
# -------------------------------------------------------
def create_user(**k):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute("""
            INSERT INTO users
            (name, email, password, matric, program, department, phone, gender, dob, hall,
             guardian_name, guardian_phone, avatar)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            k["name"], k["email"], k["password"], k["matric"], k["program"],
            k["department"], k["phone"], k["gender"], k["dob"], k["hall"],
            k["guardian_name"], k["guardian_phone"], k["avatar"]
        ))

        conn.commit()
        conn.close()
        return True, "Account created!"

    except sqlite3.IntegrityError:
        return False, "Email already exists."


# -------------------------------------------------------
# Get user by email
# -------------------------------------------------------
def get_user_by_email(email):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT name, email, matric, program, department, phone, gender,
               dob, hall, guardian_name, guardian_phone, avatar
        FROM users WHERE email = ?
    """, (email,))

    row = c.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "name": row[0],
        "email": row[1],
        "matric": row[2],
        "program": row[3],
        "department": row[4],
        "phone": row[5],
        "gender": row[6],
        "dob": row[7],
        "hall": row[8],
        "guardian_name": row[9],
        "guardian_phone": row[10],
        "avatar": row[11],
    }


# -------------------------------------------------------
# Validate Login
# -------------------------------------------------------
def validate_credentials(email, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT name, email, matric, program, department, phone, gender,
               dob, hall, guardian_name, guardian_phone, avatar
        FROM users WHERE email = ? AND password = ?
    """, (email, password))

    row = c.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "name": row[0],
        "email": row[1],
        "matric": row[2],
        "program": row[3],
        "department": row[4],
        "phone": row[5],
        "gender": row[6],
        "dob": row[7],
        "hall": row[8],
        "guardian_name": row[9],
        "guardian_phone": row[10],
        "avatar": row[11],
    }


# -------------------------------------------------------
# Email Exists?
# -------------------------------------------------------
def email_exists(email):
    return get_user_by_email(email) is not None


# -------------------------------------------------------
# Login / Logout state
# -------------------------------------------------------
def login_user(user):
    st.session_state["logged_in"] = True
    st.session_state["user"] = user

def logout_user():
    st.session_state["logged_in"] = False
    st.session_state["user"] = None
