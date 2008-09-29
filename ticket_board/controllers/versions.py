import logging

from pylons import request, response, session
from pylons import tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from ticket_board.lib.base import BaseController, render
from ticket_board.lib.ticket_store import get_ticket_store

log = logging.getLogger(__name__)

class VersionsController(BaseController):
    
    def index(self, format='html'):
        """GET /versions: All items in the collection."""
        # url_for('versions')
        pass

    def create(self):
        """POST /versions: Create a new item."""
        # url_for('versions')
        pass

    def new(self, format='html'):
        """GET /versions/new: Form to create a new item."""
        # url_for('new_version')
        pass

    def update(self, id):
        """PUT /versions/id: Update an existing item."""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(h.url_for('version', id=ID),
        #           method='put')
        # url_for('version', id=ID)
        pass

    def delete(self, id):
        """DELETE /versions/id: Delete an existing item."""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(h.url_for('version', id=ID),
        #           method='delete')
        # url_for('version', id=ID)
        pass

    def show(self, id, format='html'):
        """
        GET /versions/id: Show a specific item.
        url_for('version', id=ID)
        """
        ticket_store = get_ticket_store()
        
        project_id = request.params['project_id']
        version    = ticket_store.get_version(id, project_id)

        c.version = version
        c.issues  = version.issues()
        
        return render('/versions/show.mako')

    def edit(self, id, format='html'):
        """GET /versions/id;edit: Form to edit an existing item."""
        # url_for('edit_version', id=ID)
        pass
