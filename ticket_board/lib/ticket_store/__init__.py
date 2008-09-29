import logging

class TicketStore(object):
    def __init__(self, host, port, username, password, path=None):
        self.host = host
        self.port = port
        self.path = path
        self.username = username
        self.password = password
        
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
        return Version(self, id, name, project_id, released)

    def get_issues(self, version_id):
        for issue in self._get_issues(version_id):
            yield issue

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
        self.store  = store
        self.id     = id
        self.name   = name
        
        self.project_id = project_id 
        self.released   = released

    def issues(self):
        for issue in self.store.get_issues(self.id):
            yield issue

    def __repr__(self):
        return "[Version %s: %s]" % (str(self.id), str(self.name))

# ------------------------------------------------------------------------------
# Storage Factory
# ------------------------------------------------------------------------------

def get_ticket_store():
    from ticket_board.lib.ticket_store.jira import JiraTicketStore
    store = JiraTicketStore('localhost', 8080, username='', password='')
    store.login()
    return store