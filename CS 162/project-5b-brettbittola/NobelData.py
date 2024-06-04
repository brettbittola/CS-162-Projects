# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 10/21/2023
# Description: Opens a JSON file, reads it and searches for a list of winners based on a given year and category.

import json


class NobelData:
    """Opens a file of text, reads it and searches for a Nobel Prize winner based on the year and category."""
    def __init__(self):
        """Opens a file to read"""
        self._infile = open('nobels.json', 'r')

    def get_infile(self):
        """Returns infile, which reads nobels.json"""
        return self._infile

    def search_nobel(self, year, category):
        """Searches the list of Nobel Prizes winners and retrieves the last name of the winner
        given a year and category"""
        surnames = []
        full_values = []
        nobel_winners = json.load(self.get_infile())
        for winner in nobel_winners["prizes"]:
            if winner["year"] == year:
                if winner["category"] == category:
                    full_values = winner.get("laureates")
        for value in full_values:
            surnames.append(value['surname'])
        surnames.sort()
        return surnames
