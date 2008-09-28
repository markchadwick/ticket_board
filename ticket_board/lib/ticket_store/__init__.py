import logging

class TicketStore(object):
    def __init__(self, host, port, username, password, path=None):
        self.host = host
        self.port = port
        self.path = path
        self.username = username
        self.password = password
        
    def login(self):
        pass
        
    def logout(self):
        pass
        
    def get_tickets(self):
        pass

def get_ticket_store():
    from ticket_board.lib.ticket_store.jira import JiraTicketStore
    store = JiraTicketStore('jira', 8080, username='', password='')
    store.login()
    return store