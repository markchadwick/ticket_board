from ticket_board.tests import *

class TestTicketsController(TestController):

    def test_index(self):
        response = self.app.get(url_for('tickets'))
        # Test response...

    def test_index_as_xml(self):
        response = self.app.get(url_for('formatted_tickets', format='xml'))

    def test_create(self):
        response = self.app.post(url_for('tickets'))

    def test_new(self):
        response = self.app.get(url_for('new_ticket'))

    def test_new_as_xml(self):
        response = self.app.get(url_for('formatted_new_ticket', format='xml'))

    def test_update(self):
        response = self.app.put(url_for('ticket', id=1))

    def test_update_browser_fakeout(self):
        response = self.app.post(url_for('ticket', id=1), params=dict(_method='put'))

    def test_delete(self):
        response = self.app.delete(url_for('ticket', id=1))

    def test_delete_browser_fakeout(self):
        response = self.app.post(url_for('ticket', id=1), params=dict(_method='delete'))

    def test_show(self):
        response = self.app.get(url_for('ticket', id=1))

    def test_show_as_xml(self):
        response = self.app.get(url_for('formatted_ticket', id=1, format='xml'))

    def test_edit(self):
        response = self.app.get(url_for('edit_ticket', id=1))

    def test_edit_as_xml(self):
        response = self.app.get(url_for('formatted_edit_ticket', id=1, format='xml'))
