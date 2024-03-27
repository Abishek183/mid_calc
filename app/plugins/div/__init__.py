import logging
import sys
from app.commands import Command
from app.common import Common

class DivideCommand(Command):
    def execute(self):
        common_inst = Common()
        try:
            input1,input2 = common_inst.get_input('div')
            logging.info(f'division of {input1} and {input2} = {input1 / input2}')
            print(input1 / input2)
        except ZeroDivisionError:
            logging.error("Cannot divide by zero.")
            print('Divide by zero error')
