from ticket_board.tests import *

class TestBoardController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='board'))
        # Test response...
