import sys
from app.commands import Command
from app.history import History
import logging


class FetchCommand(Command):
    def execute(self):
        his_instance = History()
        calc_data = his_instance.read_as_data_frame().to_string(index=False)
        print('data history of calculator:\n', calc_data)
        logging.info('calculator history is fetched %s', calc_data)