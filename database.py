import sqlite3

def init_db():
    conn = sqlite3.connect('logistics.db')
    
    conn.execute('''
    CREATE TABLE IF NOT EXISTS deliveries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        supplier TEXT NOT NULL,
        payer TEXT NOT NULL,
        invoice_number TEXT NOT NULL,
        pickup_address TEXT,
        delivery_address TEXT,
        cargo_info TEXT,
        driver_id INTEGER,
        driver_name TEXT,
        author_name TEXT NOT NULL,
        status TEXT DEFAULT 'черновик',
        work_started_at TIMESTAMP,
        completed_at TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()