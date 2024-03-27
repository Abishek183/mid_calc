import logging

from app.history import History

class Common:

    def get_input(self,command):
        try:
            history_instance = History()
            input1 = float(input('enter 1st value:').strip())
            input2 = float(input('enter 2nd value:').strip())
            data = [command,input1,input2]
            existing_data = history_instance.read_as_list()
            existing_data.append(data)
            history_instance.write(existing_data)
            return input1,input2
        except ValueError:
            logging.error('error in getting inputs')
            return None,None