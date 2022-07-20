import sys
import os
import matplotlib.pyplot as plt

import_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(import_path)
sys.path.append(os.path.join(import_path, "../../"))
from data_loader.data_loader import DataLoader
from datetime import datetime, timedelta

class BigCommonTimeSeries:
    def __init__(self, data_loader: DataLoader):
        self.horizontal_data_list = data_loader.horizontal_data_list
        self.get_time_series_of_all(2)
    
    def get_time_series_of_all(self, hour_step: int):
        current_hour = self.horizontal_data_list[0][0]
        self.time_series_hours = []
        temp_delta = 0
        self.lables = []
        for i in range(len(self.horizontal_data_list)):
            if self.horizontal_data_list[i][0] < current_hour + timedelta(hours=hour_step):
                temp_delta += self.horizontal_data_list[i][4]
            else:
                self.time_series_hours.append(temp_delta)
                self.lables.append(current_hour)
                temp_delta = 0
                current_hour = self.horizontal_data_list[i][0]
        self.time_series_hours.append(temp_delta)
        self.lables.append(current_hour)
        self.plot_data_and_score(self.time_series_hours, self.lables)

    def plot_data_and_score(self, data, lables):
        f, ax = plt.subplots(1, 1, figsize=(20, 10))
        ax.plot(lables, data)
        ax.set_title(f"Money operations")
        plt.show()