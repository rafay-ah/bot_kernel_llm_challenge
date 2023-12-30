import sqlite3
import pandas as pd

class DataInterface:
    def __init__(self):
        self.conn = sqlite3.connect('data/agent_db.db')
        self.cursor = self.conn.cursor()

    def execute_query(self, sql_query):
        header = ["No.","Symbol", "Quantity", "Price", "Trade Date", "Trader Name", "Trade Type"]
        self.cursor.execute(sql_query)
        result = pd.DataFrame(self.cursor.fetchall(), columns = header)
        return result
    
    def get_schema(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        
        schema = {}
        for table in tables:
            table_name = table[0]
            self.cursor.execute(f"PRAGMA table_info({table_name});")
            columns = self.cursor.fetchall()
            schema[table_name] = [(col[1], col[2]) for col in columns]
        return schema

    def __del__(self):
        self.conn.close()
