# ------------------------------------------------------------------------------
# Global Imports
# ------------------------------------------------------------------------------
import logging
import xmlrpclib

from ticket_board.lib.ticket_store import TicketStore

log = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
# Jira Ticket Storage
# ------------------------------------------------------------------------------

class JiraTicketStore(TicketStore):
    
    def __init__(self, host, port, username, password, path=None):
        super(JiraTicketStore, self).__init__(host, port, username, password, path)
        
        self._connection_string = 'http://%s:%i/rpc/xmlrpc' % (
            self.host,
            self.port,
        )
        log.info("Connecting to %s" % self._connection_string)
        
        self._connection = xmlrpclib.ServerProxy(self._connection_string)
        self._projects = []
        self._issue_types = []
        self._auth = None

    def login(self):
        if self._auth is None:
            self._auth = self._connection.jira1.login(self.username, self.password)
            self._projects = self._connection.jira1.getProjects(self._auth)
            self._issue_types = self._connection.jira1.getIssueTypes(self._auth)

        self._load_projects()

    def logout(self):
        self._connection.logout(self._auth)
        self._auth = None
        

    def _load_projects(self):
        self._projects = []
        for project in self._connection.jira1.getProjects(self._auth):
            project = JiraProject(self._connection, self._auth, project)
            self._projects.append(project)
        
        log.info(self._projects)

class JiraProject(object):
    def __init__(self, connection, auth, params):
        self._connection = connection
        self._auth = auth
        self._key  = params['key']
        self._name = params['name']
    
        self._load_versions()
        
    def _load_versions(self):
        self._versions = []
        for version in self._connection.jira1.getVersions(self._auth, self._key):
            log.info("VERSION: %s" % str(version))
            self._versions.append(version)

    def __repr__(self):
        return '<JiraProject %s: %s>' % (self._key, self._name)