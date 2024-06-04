# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 10/4/2023
# Description: Tests LemonadeStand's classes and functions

import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand, InvalidSalesItemError

class TestLemonadeStand(unittest.TestCase):
    """Contains unit tests for the LemonadeStand project"""
    def test_item_in_stand(self):
        """Tests that an item is in the lemonade stand"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', 0.5, 1.5)
        stand.add_menu_item(item1)
        self.assertIn('lemonade', stand.get_dict())

    def test_item_not_in_stand(self):
        """Tests that an item is not in the lemonade stand"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', 0.5, 1.5)
        stand.add_menu_item(item1)
        self.assertNotIn('cookie', stand.get_dict())

    def test_menu_item_daily_sales(self):
        """Tests that an item's daily sales matches the correct number"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', 0.5, 1.5)
        stand.add_menu_item(item1)
        item3 = MenuItem('cookie', 0.2, 1)
        stand.add_menu_item(item3)
        day_0_sales = {'lemonade': 5, 'cookie': 2}
        stand.enter_sales_for_today(day_0_sales)
        self.assertEqual(stand.sales_of_menu_item_for_day(0, 'cookie'), 2)

    def test_total_menu_item_sales(self):
        """Tests that an item's total sales matches the correct number"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', 0.5, 1.5)
        stand.add_menu_item(item1)
        item3 = MenuItem('cookie', 0.2, 1)
        stand.add_menu_item(item3)
        day_0_sales = {'lemonade': 5, 'cookie': 2}
        day_1_sales = {'lemonade': 6, 'cookie': 3}
        day_2_sales = {'lemonade': 7, 'cookie': 4}
        stand.enter_sales_for_today(day_0_sales)
        stand.enter_sales_for_today(day_1_sales)
        stand.enter_sales_for_today(day_2_sales)
        self.assertEqual(stand.total_sales_for_menu_item('lemonade'), 18)

    def test_total_stand_profit(self):
        """Tests that a stand's total profit is calculated correctly"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', 0.5, 1.5)
        stand.add_menu_item(item1)
        item3 = MenuItem('cookie', 0.2, 1)
        stand.add_menu_item(item3)
        day_0_sales = {'lemonade': 5, 'cookie': 2}
        day_1_sales = {'lemonade': 6, 'cookie': 3}
        day_2_sales = {'lemonade': 7, 'cookie': 4}
        stand.enter_sales_for_today(day_0_sales)
        stand.enter_sales_for_today(day_1_sales)
        stand.enter_sales_for_today(day_2_sales)
        self.assertEqual(stand.total_profit_for_stand(), 25.2)


if __name__ == '__main__':
    """Only runs this program if it is the main file"""
    unittest.main()
