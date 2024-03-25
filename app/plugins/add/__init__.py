import logging
import sys
from app.commands import Command
from app.common import Common

class AddCommand(Command):
    def execute(self):
        common_inst = Common()
        input1,input2 = common_inst.get_input('add')
        logging.info(f'addition of {input1} and {input2} = {input1 + input2}')
        print(input1 + input2)