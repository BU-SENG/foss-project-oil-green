# services/resource_service.py

import sqlite3
import os
import datetime

DB_PATH = "database.db"
UPLOAD_FOLDER = "assets/uploads"

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ----------------------------------------------------
# 1. Initialize Resource Table
# ----------------------------------------------------
def init_resource_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            category TEXT NOT NULL,
            file_name TEXT,
            uploaded_by TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


# ----------------------------------------------------
# 2. Upload Resource (save file + insert into database)
# ----------------------------------------------------
def upload_resource(title, description, category, file, uploaded_by):

    if not title:
        return False, "Title is required."

    if not file:
        return False, "Please upload a file."

    # Save file to uploads folder
    filename = f"{datetime.datetime.now().timestamp()}_{file.name}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as f:
        f.write(file.getbuffer())

    # Insert into DB
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        INSERT INTO resources (title, description, category, file_name, uploaded_by, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        title,
        description,
        category,
        filename,
        uploaded_by,
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    ))

    conn.commit()
    conn.close()

    return True, "Resource uploaded successfully!"


# ----------------------------------------------------
# 3. List All Resources
# ----------------------------------------------------
def list_resources():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT id, title, description, category, file_name, uploaded_by, timestamp
        FROM resources
        ORDER BY id DESC
    """)

    rows = c.fetchall()
    conn.close()
    return rows


# ----------------------------------------------------
# 4. Search Resources
# ----------------------------------------------------
def search_resources(query):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    q = f"%{query.lower()}%"

    c.execute("""
        SELECT id, title, description, category, file_name, uploaded_by, timestamp
        FROM resources
        WHERE lower(title) LIKE ? OR lower(description) LIKE ?
        ORDER BY id DESC
    """, (q, q))

    rows = c.fetchall()
    conn.close()
    return rows


# ----------------------------------------------------
# 5. Filter by Category
# ----------------------------------------------------
def filter_by_category(category):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT id, title, description, category, file_name, uploaded_by, timestamp
        FROM resources
        WHERE category = ?
        ORDER BY id DESC
    """, (category,))

    rows = c.fetchall()
    conn.close()
    return rows


# ----------------------------------------------------
# 6. Count Resources
# ----------------------------------------------------
def count_resources():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM resources")
    count = c.fetchone()[0]

    conn.close()
    return count


# Auto-create table on import
init_resource_table()
