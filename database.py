import sqlite3
import pandas as pd

def run_query(query):

    conn = sqlite3.connect("analytics.db")

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df