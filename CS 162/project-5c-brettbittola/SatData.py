# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 10/31/2023
# Description: Takes data from a JSON file and converts it to a CSV file

import json


class SatData:
    """Represents a class of SAT data"""
    def __init__(self):
        """Opens a JSON file to read"""
        with open('sat.json', 'r') as self._infile:
            self._dbn_data_list = json.load(self._infile)

    def save_as_csv(self, dbn_list):
        """Writes data to a CSV file"""
        headers = ['DBN', 'School Name', 'Number of Test Takers', 'Critical Reading Mean', 'Mathematics Mean',
                   'Writing Mean']
        dbn_list.sort()
        data_list = self._dbn_data_list["data"]

        with open('output.csv', 'w') as self._outfile:
            self._outfile.write(','.join(headers) + '\n')
            for row in data_list:
                if row[8] in dbn_list:
                    row_data = [str(row[i]) for i in range(8, 14)]
                    self._outfile.write(','.join(row_data) + '\n')
