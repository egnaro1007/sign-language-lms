import sqlite3

class DatabaseMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=DatabaseMeta):
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        if params is None:
            params = []

        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return True
        
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False
        
    def fetch_all(self, query, params=None):
        if params is None:
            params = []

        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def fetch_one(self, query, params=None):
        if params is None:
            params = []

        self.cursor.execute(query, params)
        return self.cursor.fetchone()
    
    def close(self):
        self.__del__()
        
