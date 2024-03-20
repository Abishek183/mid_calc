import sys
from app.commands import Command


class DivideCommand(Command):
    def execute(self,input1, input2):
        print(input1 / input2)