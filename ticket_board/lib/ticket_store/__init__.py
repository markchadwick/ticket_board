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
        
    def get_projects(self):
        for id, name in self._get_projects():
            yield Project(self, id, name)
            
    def get_project(self, id):
        id, name = self._get_project(id)
        return Project(self, id, name)

    def get_versions(self, project_id):
        for id, name, released in self._get_versions(project_id):
            yield Version(self, id, name, released)
            
    def get_version(self, id, project_id):
        id, name, released = self._get_version(id, project_id)
        return Version(id, name, project_id, released)
        
# ------------------------------------------------------------------------------
# Project
# ------------------------------------------------------------------------------

class Project(object):
    def __init__(self, store, id, name):
        self.store = store
        self.id    = id
        self.name  = name

    def versions(self):
        for version in self.store.get_versions(self.id):
            yield version

    def __repr__(self):
        return '[Project %s: %s]' % (str(self.id), str(self.name))

# ------------------------------------------------------------------------------
# Version
# ------------------------------------------------------------------------------

class Version(object):
    def __init__(self, store, id, name, project_id, released=False):
        self.name   = name
        self.id     = id
        
        self.project_id = project_id 
        self.released   = released

    def __repr__(self):
        return "[Version %s: %s]" % (str(self.id), str(self.name))

# ------------------------------------------------------------------------------
# Storage Factory
# ------------------------------------------------------------------------------

def get_ticket_store():
    from ticket_board.lib.ticket_store.jira import JiraTicketStore
    store = JiraTicketStore('localhost', 8080, username='mark', password='imim42')
    store.login()
    return store