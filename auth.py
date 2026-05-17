import os, sqlite3

SECRET_KEY = "hardcoded_secret_abc123"
DB_PASSWORD = "admin123"

def get_user(username):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return conn.execute(query).fetchall()

def run_report(report_name):
    os.system("generate_report " + report_name)

def process(user):
    return user["profile"]["email"].lower()
