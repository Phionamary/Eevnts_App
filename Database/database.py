import psycopg2

class DatabaseConnection:
    
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", port="5433", database="Phionamary", user="Phionamary", password="phii100996")
        
    def create_cursor(self):
        self.cur = self.conn.cursor()
        return self.cur
        
        
    def create_users_table(self, user_id, first_name, last_name, email, age, password):
        Users = """CREATE TABLE IF NOT EXISTS Users(user_id serial PRIMARY KEY, 
        first_name varchar (50) NOT NULL, 
        last_name varchar (50) NOT NULL, 
        age smallint (2) NOT NULL, 
        email varchar (50) NOT NULL, 
        password varchar (50) NOT NULL, 
        created_at date)"""

        self.cur.execute(Users)


    def create_events_table(self, event_id, event_name, price, location):
        Events = """CREATE TABLE IF NOT EXISTS Event(event_id serial PRIMARY KEY, 
        event_name varchar (50) NOT NULL, 
        price int (20) NOT NULL, 
        location varchar (25) NOT NULL)"""

        self.cur.execute(Events)


    def create_tickets_table(self, ticket_id, user_id, event_id, is_valid, verification_code, created_at):
        Tickets = """CREATE TABLE IF NOT EXISTS Ticket(ticket_id serial PRIMARY KEY, 
        user_id int REFERENCES Users(user_id), event_id int REFERENCES Event(event_id), 
        is_valid boolean (3) NOT NULL, 
        verification_code varchar (20) NOT NULL, 
        created_at date)"""

        self.cur.execute(Tickets)


    def close_database_connection(self):
        self.conn.commit()
        self.conn.close()




    

        


