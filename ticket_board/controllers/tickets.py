import logging

from pylons import request, response, session
from pylons import tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from ticket_board.lib.base import BaseController, render

from ticket_board.lib.ticket_store import get_ticket_store

log = logging.getLogger(__name__)

class TicketsController(BaseController):
    
    def index(self, format='html'):
        """
        GET /tickets: All items in the collection.
        """
        ticket_store = get_ticket_store()
        # url_for('tickets')

    def create(self):
        """
        POST /tickets: Create a new item.
        """
        # url_for('tickets')
        pass

    def new(self, format='html'):
        """
        GET /tickets/new: Form to create a new item.
        """
        # url_for('new_ticket')
        pass

    def update(self, id):
        """
        PUT /tickets/id: Update an existing item.
        """
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(h.url_for('ticket', id=ID),
        #           method='put')
        # url_for('ticket', id=ID)
        pass

    def delete(self, id):
        """
        DELETE /tickets/id: Delete an existing item.
        """
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(h.url_for('ticket', id=ID),
        #           method='delete')
        # url_for('ticket', id=ID)
        pass

    def show(self, id, format='html'):
        """
        GET /tickets/id: Show a specific item.
        """
        # url_for('ticket', id=ID)
        pass

    def edit(self, id, format='html'):
        """
        GET /tickets/id;edit: Form to edit an existing item.
        """
        # url_for('edit_ticket', id=ID)
        pass
