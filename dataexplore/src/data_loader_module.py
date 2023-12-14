import pandas as pd
import sqlite3

class DataLoader:
    def __init__(self):
        pass

    @staticmethod
    def load_csv(file_path):
        """
        Load data from a CSV file.
        """
        try:
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return None

    @staticmethod
    def load_excel(file_path, sheet_name=0):
        """
        Load data from an Excel file.
        """
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            return df
        except Exception as e:
            print(f"Error loading Excel file: {e}")
            return None

    @staticmethod
    def load_json(file_path):
        """
        Load data from a JSON file.
        """
        try:
            df = pd.read_json(file_path)
            return df
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return None

    @staticmethod
    def load_sqlite(db_path, query):
        """
        Load data from a SQLite database.
        """
        try:
            conn = sqlite3.connect(db_path)
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error loading data from SQLite: {e}")
            return None