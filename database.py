import sqlite3

# Connect to or create the database
def get_connection():
    return sqlite3.connect("chat_history.database", check_same_thread=False)

# Initialize the table
def init_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Save a message
def save_message(role, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()

# Load all messages
def load_messages():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT role, content FROM messages")
    messages = cursor.fetchall()
    conn.close()
    return [{"role": role, "content": content} for role, content in messages]

# Clear all messages
def clear_messages():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM messages")
    conn.commit()
    conn.close()
