import logging

class Common:

    def get_input(self):
        try:
            input1 = float(input('enter 1st value:').strip())
            input2 = float(input('enter 2nd value:').strip())
            return input1,input2
        except ValueError:
            logging.info('error in getting inputs')