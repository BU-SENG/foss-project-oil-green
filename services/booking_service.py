# services/booking_service.py

import sqlite3
from datetime import datetime

DB_PATH = "database.db"

CAMPUS_LOCATIONS = [
    "BUCODEL Room 1",
    "BUCODEL Room 2",
    "BUCODEL Room 3",
    "BUCODEL Lab 1",
    "BUCODEL Lab 2",
    "CIT Lab",
    "SCLT",
    "WRA",
]


# ------------------------------------------------
# Create booking table
# ------------------------------------------------
def init_booking_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            location TEXT,
            user_email TEXT,
            date TEXT,
            start_time TEXT,
            end_time TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


# ------------------------------------------------
# Count bookings for a user
# ------------------------------------------------
def count_bookings(user_email):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM bookings WHERE user_email = ?", (user_email,))
    result = c.fetchone()[0]

    conn.close()
    return result


# ------------------------------------------------
# List bookings for a user
# ------------------------------------------------
def list_user_bookings(user_email):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT title, location, date, start_time, end_time, created_at
        FROM bookings
        WHERE user_email = ?
        ORDER BY id DESC
    """, (user_email,))

    rows = c.fetchall()
    conn.close()

    return rows


# ------------------------------------------------
# Check availability
# ------------------------------------------------
def check_availability(location, date, start_dt, end_dt):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT * FROM bookings
        WHERE location = ?
        AND date = ?
        AND (
            (start_time <= ? AND end_time >= ?)
            OR
            (start_time <= ? AND end_time >= ?)
        )
    """, (location, date, start_dt, start_dt, end_dt, end_dt))

    conflict = c.fetchone()
    conn.close()

    return conflict is None  # True = available


# ------------------------------------------------
# CREATE BOOKING (NOW ACCEPTS TITLE)
# ------------------------------------------------
def create_booking(title, location, user_email, date, start_dt, end_dt):
    if not check_availability(location, date, start_dt, end_dt):
        return False, "This time slot is already booked."

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        INSERT INTO bookings (title, location, user_email, date, start_time, end_time, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        title,
        location,
        user_email,
        str(date),
        start_dt,
        end_dt,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()
    return True, "Booking successfully created!"
