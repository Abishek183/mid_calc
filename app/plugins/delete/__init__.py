import sys
from app.commands import Command
from app.history import History
import logging


class DeleteCommand(Command):
    def execute(self,input1, input2):
        his_instance = History()
        existing_data = his_instance.read_as_data_frame()
        record_id = int(input('enter the id for record to delete:'))
        updated_data = existing_data[existing_data['ID'] != record_id]
        logging.info(f'history record of id {record_id} is deleted in ',existing_data)
        print('data history of calculator after delete:\n', updated_data.to_string(index=False))
        his_instance.write(updated_data.values.tolist())
