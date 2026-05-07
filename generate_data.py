import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

conn = sqlite3.connect("analytics.db")
cursor = conn.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    country TEXT,
    signup_date TEXT
)
""")

# SESSIONS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS sessions (
    session_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    session_date TEXT
)
""")

# TRANSACTIONS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount REAL,
    transaction_date TEXT
)
""")

countries = ["US", "IN", "UK", "CA"]

# INSERT USERS
for i in range(1, 5001):

    signup_date = fake.date_between(
        start_date="-90d",
        end_date="today"
    )

    cursor.execute("""
    INSERT INTO users (user_id, country, signup_date)
    VALUES (?, ?, ?)
    """, (
        i,
        random.choice(countries),
        signup_date.strftime("%Y-%m-%d")
    ))

# INSERT SESSIONS
for i in range(1, 50001):

    session_date = fake.date_between(
        start_date="-30d",
        end_date="today"
    )

    cursor.execute("""
    INSERT INTO sessions (session_id, user_id, session_date)
    VALUES (?, ?, ?)
    """, (
        i,
        random.randint(1, 5000),
        session_date.strftime("%Y-%m-%d")
    ))

# INSERT TRANSACTIONS
for i in range(1, 10001):

    transaction_date = fake.date_between(
        start_date="-30d",
        end_date="today"
    )

    cursor.execute("""
    INSERT INTO transactions (
        transaction_id,
        user_id,
        amount,
        transaction_date
    )
    VALUES (?, ?, ?, ?)
    """, (
        i,
        random.randint(1, 5000),
        round(random.uniform(5, 100), 2),
        transaction_date.strftime("%Y-%m-%d")
    ))

conn.commit()
conn.close()

print("Database created successfully!")