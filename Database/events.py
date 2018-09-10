import psycopg2
from Database.database import DatabaseConnection


class Events():
    def __init__(self, event_id, event_name, price, location):
        self.event_id = event_id
        self.event_name = event_name
        self.price = price
        self.location = location
        self.conn = psycopg2.connect(host="localhost", port="5433", database="Phionamary", user="Phionamary", password="phii100996")

    def create_cursor(self):
        self.cur = self.conn.cursor()
        return self.cur

    def add_new_event(self):
        new_event = """INSERT INTO Events(event_name, price, location) 
        VALUES ('{}', '{}', '{}')""".format(self.event_name, self.price, self.location)        
        self.cur.execute(new_event)
        self.conn.commit()
        return True 

    def get_event_by_id(self): 
        event = """SELECT * FROM Events WHERE event_id="{}" """.format(self.event_id)
        self.cur.execute(event)     
        return self.cur.fetchone() 

    def get_all_events(self):
        all_events = """SELECT * FROM Events """
        self.cur.execute(all_events)
        return self.cur.fetchall() 