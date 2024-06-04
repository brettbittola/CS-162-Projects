# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 10/4/2023
# Description: A lemonade stand that tracks how many of each menu item are sold on each day.

class MenuItem:
    """Represents an item at a lemonade stand with a name, wholesale cost and price"""
    def __init__(self, name, cost, price):
        self._name = name
        self._wholesale_cost = cost
        self._selling_price = price

    def get_name(self):
        """Returns the name of the item"""
        return self._name

    def get_wholesale_cost(self):
        """Returns the wholesale cost of the item"""
        return self._wholesale_cost

    def get_selling_price(self):
        """Returns the selling price of the item"""
        return self._selling_price


class SalesForDay:
    """Represents a total number of sales for one day of menu items at the lemonade stand"""
    def __init__(self, days, sales_dict):
        self._days = days
        self._sales_dict = sales_dict

    def get_day(self):
        """Returns the number of days the stand has been open"""
        return self._days

    def get_sales_dict(self):
        """Returns a dictionary with the names of items sold and how many were sold that day"""
        return self._sales_dict


class InvalidSalesItemError(Exception):
    """Error that is raised when an item not on the menu is added to the sales dictionary"""
    pass


class LemonadeStand:
    def __init__(self, name):
        self._name = name
        self._day = 0
        self._dict = {}
        self._list = []

    def get_name(self):
        """Returns the name of the lemonade stand"""
        return self._name

    def get_day(self):
        """Returns the number of days the lemonade stand has operated"""
        return self._day

    def get_dict(self):
        """Returns a dictionary of items sold at the lemonade stand"""
        return self._dict

    def add_menu_item(self, MenuItem):
        """Adds a menu item to the lemonade stand"""
        self._dict[MenuItem.get_name()] = MenuItem.get_wholesale_cost(), MenuItem.get_selling_price()

    def enter_sales_for_today(self, sales_for_day_dict):
        """Adds a SalesForDay object to a list, and checks that all items sold are on the menu"""
        for key in sales_for_day_dict:
            if key not in self._dict:
                raise InvalidSalesItemError("This item is not for sale at this stand.")
        self._list.append(SalesForDay(self._day, sales_for_day_dict))
        self._day += 1
        return self._list

    def sales_of_menu_item_for_day(self, day, item):
        """Returns the number of a given item sold on that day"""
        daily_menu_item_sales = 0
        for daily_sales in self._list:
            if daily_sales.get_day() == day:
                daily_menu_item = daily_sales.get_sales_dict()
                if item in daily_menu_item:
                    daily_menu_item_sales = daily_menu_item[item]
        return daily_menu_item_sales

    def total_sales_for_menu_item(self, item):
        """Returns the total number of a menu item that was sold at the stand"""
        total_item_sales = 0
        for day in self._list:
            total_item_sales += self.sales_of_menu_item_for_day(day.get_day(), item)
        return total_item_sales

    def total_profit_for_menu_item(self, item):
        """Returns the total profit for an item sold at the stand"""
        price = self._dict[item][1]
        cost = self._dict[item][0]
        sales = self.total_sales_for_menu_item(item)
        total_item_profit = (price - cost) * sales
        return total_item_profit

    def total_profit_for_stand(self):
        """Returns the total profit for all items sold for the history of the stand"""
        total_stand_profit = 0
        for item in self._dict:
            total_stand_profit += self.total_profit_for_menu_item(item)
        return total_stand_profit


def main():
    """"Test code that only runs if this is the main file in the folder"""
    stand = LemonadeStand("Lemmy's Lemons")
    tea = MenuItem('tea', 0.9, 1.8)
    stand.add_menu_item(tea)
    chips = MenuItem('chips', 0.3, 1)
    stand.add_menu_item(chips)
    day_2_sales = {'tea': 9, 'chips': 7, 'hamburger': 8}
    try:
        stand.enter_sales_for_today(day_2_sales)
    except InvalidSalesItemError:
        print("This item is not for sale at this stand.")


if __name__ == '__main__':
    """Only runs this code if it is the main file"""
    main()
