# services/contact_service.py

import sqlite3

DB_PATH = "database.db"


# ---------------------------------------------------------
# INIT CONTACT TABLE
# ---------------------------------------------------------
def init_contact_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT,
            department TEXT,
            phone TEXT,
            email TEXT
        )
    """)

    # Check if empty
    c.execute("SELECT COUNT(*) FROM contacts")
    empty = c.fetchone()[0] == 0

    if empty:
        default_contacts = [
            ("Dr. Adewale Adebayo", "HOD, Computer Science", "Computing & Engineering",
             "+2347030001111", "adebayoa@babcock.edu.ng"),

            ("Mrs. Dorcas Akinlabi", "Registrar", "Registry Department",
             "+2347030002222", "akinlabid@babcock.edu.ng"),

            ("Mr. Emmanuel Ojo", "Hall Administrator", "Male Halls Management",
             "+2347030003333", "ojoe@babcock.edu.ng"),

            ("Mrs. Peace Nwankwo", "Hall Administrator", "Female Halls Management",
             "+2347030004444", "nwankwop@babcock.edu.ng"),

            ("Dr. Kingsley Orji", "Academic Advisor", "Computing & Engineering",
             "+2347030005555", "orjik@babcock.edu.ng"),
        ]

        c.executemany("""
            INSERT INTO contacts (name, role, department, phone, email)
            VALUES (?, ?, ?, ?, ?)
        """, default_contacts)

    conn.commit()
    conn.close()


# Initialize table on import
init_contact_table()


# ---------------------------------------------------------
# FETCH ALL CONTACTS
# ---------------------------------------------------------
def get_all_contacts():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT name, role, department, phone, email
        FROM contacts
        ORDER BY name ASC
    """)

    rows = c.fetchall()
    conn.close()

    contacts = []
    for r in rows:
        contacts.append({
            "name": r[0],
            "role": r[1],
            "department": r[2],
            "phone": r[3],
            "email": r[4],
        })

    return contacts


# ---------------------------------------------------------
# COUNT CONTACTS (Dashboard)
# ---------------------------------------------------------
def count_contacts():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM contacts")
    result = c.fetchone()[0]

    conn.close()
    return result


# ---------------------------------------------------------
# SEARCH CONTACTS
# ---------------------------------------------------------
def search_contacts(query: str):
    q = query.lower()

    results = []
    for c in get_all_contacts():
        if (q in c["name"].lower() or
            q in c["role"].lower() or
            q in c["department"].lower() or
            q in c["email"].lower()):
            results.append(c)

    return results


# ---------------------------------------------------------
# COMPATIBILITY WRAPPER
# Old pages expect filter_contacts, new code uses search_contacts
# ---------------------------------------------------------
def filter_contacts(query: str):
    return search_contacts(query)
