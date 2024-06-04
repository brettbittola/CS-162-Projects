# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 10/21/2023
# Description: A class of neighborhood pets, that can add or remove pets from a dictionary. Also reads and writes data
#              to a JSON file.

import json


class NeighborhoodPets:
    """Creates a class representing neighborhood pets."""
    def __init__(self):
        """Creates a dictionary of pets, along with their species type and owner's name."""
        self._pet_list = {}

    def get_pet_list(self):
        """Returns the list of pets"""
        return self._pet_list

    def add_pet(self, pet_name, species, pet_owner):
        """Adds a pet to a list of pets, with name, species and pet owner attributes"""
        if pet_name not in self._pet_list:
            new_pet = {
                "species": species,
                "pet owner": pet_owner
            }
            self._pet_list[pet_name] = new_pet
        else:
            raise DuplicateNameError("Pet with that name already in list.")

    def delete_pet(self, pet_name):
        """Removes a pet from the list"""
        del self._pet_list[pet_name]

    def get_owner(self, pet_name):
        """Returns the name of a given pet's owner."""
        if pet_name in self._pet_list:
            return self._pet_list[pet_name]['pet owner']

    def save_as_json(self, file_name):
        """Saves data to a file with a given file_name parameter"""
        with open(file_name, 'w') as outfile:
            json.dump(self._pet_list, outfile)

    def read_json(self, file_name):
        """Loads and reads data from a JSON file"""
        with open(file_name, 'r') as infile:
            self._pet_list = json.load(infile)

    def get_all_species(self):
        """Returns a Python set of the species of all pets"""
        species_list = set()
        for pet in self._pet_list.values():
            species_list.add(pet['species'])
        return species_list


class DuplicateNameError(Exception):
    """Raises an error if a pet is added with the same name as another pet."""
