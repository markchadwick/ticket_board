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
    
    def __init__(self, host, port, username, password):
        super(JiraTicketStore, self).__init__(host, port, username, password, None)
        
        self._connection_string = 'http://%s:%i/rpc/xmlrpc' % (
            self.host,
            self.port)
        
        self._connection = xmlrpclib.ServerProxy(self._connection_string)
        self._auth = None

    def login(self):
        if self._auth is None:
            self._auth = self._connection.jira1.login(self.username, self.password)

    def logout(self):
        self._connection.logout(self._auth)
        self._auth = None
        
    def _get_projects(self):
        for project in self._connection.jira1.getProjects(self._auth):
            yield project['key'], project['name']

    def _get_project(self, id):
        for project_id, project_name in self._get_projects():
            if project_id == id:
                return project_id, project_name
                
    def _get_versions(self, project_id):
        for version in self._connection.jira1.getVersions(self._auth, project_id):
            yield version['id'], version['name'], version['released']
            
    def _get_version(self, id, project_id):
        for version_id, version_name, version_released in self._get_versions(project_id):
            if version_id == id:
                return version_id, version_name, version_released
                
    def _get_issues(self, version_id):
        for issue in self._connection.jira1.getIssuesFromTextSearchWithProject(
                                            self._auth,
                                            [version_id],
                                            '',
                                            100
                                            ):
            yield issue