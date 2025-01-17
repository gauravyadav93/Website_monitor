import sqlite3
from app.models import Site, SiteCreate

DATABASE = 'monitoring.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def add_site(site: SiteCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sites (url, check_interval_seconds, name, expected_status_code) VALUES (?, ?, ?, ?)',
                   (site.url, site.check_interval_seconds, site.name, site.expected_status_code))
    conn.commit()
    site_id = cursor.lastrowid
    conn.close()
    return {**site.dict(), "id": site_id}

def remove_site(site_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM sites WHERE id = ?', (site_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def get_sites():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sites')
    sites = cursor.fetchall()
    conn.close()
    return [dict(site) for site in sites]

def get_site_history(site_id: int):
    # This function would need to be implemented to track history
    pass