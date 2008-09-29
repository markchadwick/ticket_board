# ------------------------------------------------------------------------------
# Global Imports
# ------------------------------------------------------------------------------

import logging

from pylons import request, response, session
from pylons import tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from ticket_board.lib.base import BaseController, render
from ticket_board.lib.ticket_store import get_ticket_store

log = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
# Project Resource
# ------------------------------------------------------------------------------

class ProjectsController(BaseController):
    
    def index(self, format='html'):
        """
        GET /projects: All items in the collection.
        url_for('projects')
        """
        ticket_store = get_ticket_store()
        c.projects = ticket_store.get_projects()
        
        return render('/projects/list.mako')

    def create(self):
        """
        POST /projects: Create a new item.
        url_for('projects')
        """
        pass

    def new(self, format='html'):
        """GET /projects/new: Form to create a new item."""
        # url_for('new_project')
        pass

    def update(self, id):
        """PUT /projects/id: Update an existing item."""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(h.url_for('project', id=ID),
        #           method='put')
        # url_for('project', id=ID)
        pass

    def delete(self, id):
        """DELETE /projects/id: Delete an existing item."""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(h.url_for('project', id=ID),
        #           method='delete')
        # url_for('project', id=ID)
        pass

    def show(self, id, format='html'):
        """
        GET /projects/id: Show a specific item.
        url_for('project', id=ID)
        """
        ticket_store = get_ticket_store()
        project = ticket_store.get_project(id)
        
        c.project  = project
        c.versions = project.versions()

        return render('/projects/show.mako')

    def edit(self, id, format='html'):
        """GET /projects/id;edit: Form to edit an existing item."""
        # url_for('edit_project', id=ID)
        pass
