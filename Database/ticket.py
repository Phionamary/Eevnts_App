import psycopg2
from Database.database import DatabaseConnection

class Ticket():
    def __init__(self, ticket_id, user_id, event_id, is_valid, verification_code, created_at):
        self.ticket_id = ticket_id
        self.user_id = user_id
        self.event_id = event_id
        self.is_valid = is_valid
        self.verification_code = verification_code
        self.created_at = created_at
        self.conn = psycopg2.connect(host="localhost", port="5433", database="Phionamary", user="Phionamary", password="phii100996")

    def create_cursor(self):
        self.cur = self.conn.cursor()
        return self.cur


    def create_new_ticket(self):
        new_ticket = """INSERT INTO Tickets(user_id,event_id,is_valid,verification_code,created_at)
        VALUES ('{}', '{}', '{}', '{}', '{}');""".format(self.user_id,self.event_id,self.is_valid, self.verification_code,self.created_at)      
        self.cur.execute(new_ticket)
        self.conn.commit()
        return "This ticket has been created for: "

    def get_ticket_by_id(self):
        ticket = """SELECT FROM Tickets where ticket_id="{0}" AND user_id="{1}" """.format(self.ticket_id, self.user_id)
        self.cur.execute(ticket)
        single_ticket = self.cur.fetchone() 
        return single_ticket

    def get_all_tickets(self):
        all_tickets = """SELECT * FROM Tickets WHERE user_id='{}'""".format(self.user_id)
        self.cur.execute(all_tickets)
        tickets = self.cur.fetchall() 
        return tickets
    