"""Setup the ticket_board application"""
import logging

from ticket_board.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup ticket_board here"""
    load_environment(conf.global_conf, conf.local_conf)
