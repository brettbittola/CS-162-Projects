# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 10/9/2023
# Description: A library that keeps track of items rented and who rented them.


class LibraryItem:
    """Represents an item in a library"""
    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_library_item_id(self):
        """Return library item ID"""
        return self._library_item_id

    def get_location(self):
        """Returns an item's location"""
        # a LibraryItem can be "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT"
        return self._location

    def set_location(self, location):
        """Sets a new location for the library item"""
        self._location = location

    def get_checked_out_by(self):
        """"Returns patron that has currently checked out a library item"""
        return self._checked_out_by

    def set_checked_out_by(self, patron):
        """Sets the patron that has checked out a library item"""
        self._checked_out_by = patron

    def get_requested_by(self):
        """Returns the patron that has requested a library item"""
        return self._requested_by

    def set_requested_by(self, patron):
        """Sets the patron that has requested a library item"""
        self._requested_by = patron

    def get_date_checked_out(self):
        """Returns the date a library item was checked out"""
        return self._date_checked_out

    def set_date_checked_out(self, date):
        """Sets the date a library item was checked out"""
        self._date_checked_out = date


class Book(LibraryItem):
    """Represents a book in a library, subclass of LibraryItem"""
    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author
        self._check_out_length = 21

    def get_author(self):
        """Returns the book's author"""
        return self._author

    def get_check_out_length(self):
        """Returns the number of days a library item may be checked out"""
        return self._check_out_length


class Album(LibraryItem):
    """Represents an album in a library, subclass of LibraryItem"""
    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist
        self._check_out_length = 14

    def get_artist(self):
        """Returns the album's artist"""
        return self._artist

    def get_check_out_length(self):
        """Returns the number of days a library item may be checked out"""
        return self._check_out_length


class Movie(LibraryItem):
    """Represents a movie in a library, subclass of LibraryItem"""
    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director
        self._check_out_length = 7

    def get_director(self):
        """Returns the movie's director"""
        return self._director

    def get_check_out_length(self):
        """Returns the number of days a library item may be checked out"""
        return self._check_out_length


class Patron:
    """Represents a patron of the library"""
    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_fine_amount(self):
        """Returns the amount a patron owes"""
        return self._fine_amount

    def get_patron_id(self):
        """Returns a patron's ID"""
        return self._patron_id

    def get_checked_out_items(self):
        """Returns a list of a patron's checked out items"""
        return self._checked_out_items

    def add_library_item(self, library_item_object):
        """Adds a library item to a patron's checked out items"""
        self._checked_out_items.append(library_item_object)

    def remove_library_item(self, item):
        """Removes a library item from a patron's checked out items"""
        if item in self._checked_out_items:
            self._checked_out_items.remove(item)

    def amend_fine(self, amount):
        """Adjusts the amount a patron owns by given parameter"""
        self._fine_amount += amount
        return self._fine_amount


class Library:
    """Represents a library class with a list of patrons and items, as well as methods to adjust who is renting what
     item and methods to adjust fines."""
    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def get_current_date(self):
        """Returns the current date"""
        return self._current_date

    def add_library_item(self, item):
        """Adds a library item to the holdings list"""
        self._holdings.append(item)

    def add_patron(self, person):
        """Adds a patron to the members list"""
        self._members.append(person)

    def lookup_library_item_from_id(self, library_item_id):
        """Returns a LibraryItem object from a library item ID string"""
        library_item_object = None
        for library_item in self._holdings:
            if library_item.get_library_item_id() == library_item_id:
                library_item_object = library_item
        return library_item_object

    def lookup_patron_from_id(self, patron_id):
        """Returns a Patron object from the patron ID string"""
        patron_id_object = None
        for patron in self._members:
            if patron_id == patron.get_patron_id():
                patron_id_object = patron
        return patron_id_object

    def check_out_library_item(self, patron_id, library_item_id):
        """Adds a library item to a patron's checked out items and updates item's location"""
        patron = self.lookup_patron_from_id(patron_id)
        library_item = self.lookup_library_item_from_id(library_item_id)

        if patron not in self._members:
            return "patron not found"
        if library_item not in self._holdings:
            return "item not found"

        if library_item.get_location() == "CHECKED_OUT":
            return "item already checked out"
        elif library_item.get_location() == "ON_HOLD_SHELF":
            if library_item.get_requested_by() != patron_id:
                return "item on hold by other patron"
        else:
            library_item.set_checked_out_by(patron)
            library_item.set_date_checked_out(self._current_date)
            library_item.set_location("CHECKED_OUT")
            patron.add_library_item(library_item)
            if library_item.get_requested_by() == patron_id:
                library_item.set_requested_by(None)
            return "check out successful"

    def return_library_item(self, library_item_id):
        """Removes a library item from a patron's checked_out_items and returns it to the library's holdings"""
        library_item = self.lookup_library_item_from_id(library_item_id)
        if library_item in self._holdings:
            if library_item.get_location() == "CHECKED_OUT":
                patron = library_item.get_checked_out_by()
                patron.remove_library_item(library_item_id)
                library_item.set_checked_out_by(None)
                if library_item.get_requested_by() is True:
                    library_item.set_location("ON_HOLD_SHELF")
                    return "return successful"
                else:
                    library_item.set_location("ON_SHELF")
                    return "return successful"
            else:
                return "item already in library"
        else:
            return "item not found"

    def request_library_item(self, patron_id, library_item_id):
        """Adds a library item to a patron's requested_by list"""
        patron = self.lookup_patron_from_id(patron_id)
        library_item = self.lookup_library_item_from_id(library_item_id)

        if patron not in self._members:
            return "patron not found"
        if library_item not in self._holdings:
            return "item not found"

        if library_item.get_requested_by() is not None:
            return "item already on hold"
        else:
            library_item.set_requested_by(patron)
            if library_item.get_location() == "ON_SHELF":
                library_item.set_location("ON_HOLD_SHELF")
            return "request successful"

    def pay_fine(self, patron_id, amount):
        """Adjusts patron's fine if they are a library member"""
        patron = self.lookup_patron_from_id(patron_id)

        if patron not in self._members:
            return "patron not found"
        else:
            patron.amend_fine(-amount)
            return "payment successful"

    def increment_current_date(self):
        """Increases date by one and increases fines by 10 cents for each overdue item"""
        self._current_date += 1
        for patron in self._members:
            for item in patron.get_checked_out_items():
                if item is not None:
                    rented_days = self._current_date - item.get_date_checked_out()
                    if rented_days > item.get_check_out_length():
                        patron.amend_fine(0.10)
