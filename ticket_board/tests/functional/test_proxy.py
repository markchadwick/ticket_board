from ticket_board.tests import *

class TestProxyController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='proxy'))
        # Test response...
