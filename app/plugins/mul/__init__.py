import sys
from app.commands import Command
from app.common import Common

class MultiplyCommand(Command):
    def execute(self):
        common_inst = Common()
        input1,input2 = common_inst.get_input()
        print(input1 * input2)