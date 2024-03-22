import os
import logging
import pandas as pd

class History:
    def __init__(self, path='./data/calc_history.csv'):
        self.path = path
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
            logging.info(f"The directory '{os.path.dirname(path)}' is created.")

        elif not os.access(os.path.dirname(path), os.W_OK):
            logging.error(f"The directory '{os.path.dirname(path)}' is not writable.")

    def write(self, data):
        cal_data = pd.DataFrame(data, columns=['action', 'value1', 'value2'])
        cal_data.to_csv(self.path, index=False)
    
    def read(self):
        existing_data = pd.read_csv(self.path)
        return existing_data.values.tolist()
