from app.commands import Command
from app.common import Common
import logging

class SubtractCommand(Command):
    def execute(self):
        common_inst = Common()
        input1,input2 = common_inst.get_input('sub')
        logging.info(f'Subtract of {input1} and {input2} = {input1 - input2}')
        print(input1 - input2)