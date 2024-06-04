# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 10/17/2023
# Description: Creates a box class and sorts boxes from most to least volume using insertion sort.

class Box:
    """Represents a box with length, width and height parameters."""
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """Returns the boxes length"""
        return self._length

    def get_width(self):
        """Returns the boxes width"""
        return self._width

    def get_height(self):
        """Returns the boxes height"""
        return self._height

    def volume(self):
        """Calculates the boxes volume"""
        volume = self._length * self._width * self._height
        return volume


def box_sort(box_list):
    """Sorts a list of Boxes from greatest volume to least volume using insertion sort."""
    for box in range(1, len(box_list)):
        box_volume = box_list[box]
        pos = box - 1
        while pos >= 0 and box_volume.volume() > box_list[pos].volume():
            box_list[pos + 1] = box_list[pos]
            pos -= 1
        box_list[pos + 1] = box_volume
