"""Pylons application test package

This package assumes the Pylons environment is already loaded, such as
when this script is imported from the `nosetests --with-pylons=test.ini`
command.

This module initializes the application via ``websetup`` (`paster
setup-app`) and provides the base testing objects.
"""
from unittest import TestCase

from paste.deploy import loadapp
from paste.fixture import TestApp
from paste.script.appinstall import SetupCommand
from pylons import config
from routes import url_for

import pylons.test

__all__ = ['url_for', 'TestController']

# Invoke websetup with the current config file
SetupCommand('setup-app').run([config['__file__']])

class TestController(TestCase):

    def __init__(self, *args, **kwargs):
        if pylons.test.pylonsapp:
            wsgiapp = pylons.test.pylonsapp
        else:
            wsgiapp = loadapp('config:%s' % config['__file__'])
        self.app = TestApp(wsgiapp)
        TestCase.__init__(self, *args, **kwargs)
