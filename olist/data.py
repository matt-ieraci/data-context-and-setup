import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/csv')
        
        file_names = [file for file in os.listdir(csv_path) if file != ".keep"]
        key_names = [name.replace(".csv", "").replace("_dataset", "").replace("olist_", "") for name in file_names]
        
        data = {}
        for key, file_name in zip(key_names, file_names):
            data[key] = pd.read_csv(os.path.join(csv_path, file_name))
            
        return data
            
    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")