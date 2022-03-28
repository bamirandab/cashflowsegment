import psycopg2
import os
from dotenv import load_dotenv


class PostgresSqlProvider:

    def __init__(self):
        load_dotenv()
        self.client = psycopg2.connect(host=os.getenv("SQL_HOST_NAME"),
                                       port=os.getenv("SQL_PORT"),
                                       user=os.getenv("SQL_USER_NAME"),
                                       password=os.getenv("SQL_PASSWORD"),
                                       database=os.getenv("SQL_DATABASE"))
        self.cursor = self.client.cursor()

    def execute_query(self, query, params):
        self.cursor.execute(query, params)
        
