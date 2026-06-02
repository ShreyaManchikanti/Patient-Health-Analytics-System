# main.py

from load_dataset_module import PatientDataLoader
from statistics_module import StatisticsCalculator
from query_module import PatientQuery
from user_interface_module import PatientGUI

def main():

    loader = PatientDataLoader("E:\data\data.csv")
    data = loader.load_data()

    stats = StatisticsCalculator()
    query = PatientQuery(data, stats)

    gui = PatientGUI(query, stats)
    gui.run()

if __name__ == "__main__":
    main()
