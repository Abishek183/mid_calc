import sys
from app.commands import Command
from app.history import History
import logging


class ClearCommand(Command):
    def execute(self,input1, input2):
        his_instance = History()
        his_instance.clear()
        logging.info('calculator history is cleared')