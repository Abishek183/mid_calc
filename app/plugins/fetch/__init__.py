import sys
from app.commands import Command
from app.history import History
import logging


class FetchCommand(Command):
    def execute(self,input1, input2):
        his_instance = History()
        calc_data = his_instance.read_as_list()
        print('data history of calculator:', calc_data)
        logging.info('calculator history is fetched %s', calc_data)