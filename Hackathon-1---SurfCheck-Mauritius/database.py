import sqlite3

def init_db():
    conn = sqlite3.connect("surf.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS surf_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT,
        weather TEXT,
        wind_speed REAL,
        temp REAL
    )''')
    conn.commit()
    conn.close()

def save_surf_log(location, weather, wind_speed, temp):
    conn = sqlite3.connect("surf.db")
    c = conn.cursor()
    c.execute("INSERT INTO surf_log (location, weather, wind_speed, temp) VALUES (?, ?, ?, ?)",
              (location, weather, wind_speed, temp))
    conn.commit()
    conn.close()
