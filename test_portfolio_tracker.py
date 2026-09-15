"""
Unit tests for StockPortfolioTracker
"""

import os
import unittest
from portfolio_tracker import StockPortfolioTracker, DEFAULT_STOCK_PRICES


class TestStockPortfolioTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = StockPortfolioTracker()

    def test_default_prices(self):
        self.assertEqual(self.tracker.get_price("AAPL"), 180.0)
        self.assertEqual(self.tracker.get_price("TSLA"), 250.0)
        self.assertEqual(self.tracker.get_price("aapl"), 180.0)

    def test_add_stock_valid(self):
        success, msg = self.tracker.add_stock("AAPL", 10)
        self.assertTrue(success)
        self.assertIn("AAPL", self.tracker.portfolio)
        self.assertEqual(self.tracker.portfolio["AAPL"], 10)

    def test_add_stock_invalid(self):
        success, msg = self.tracker.add_stock("UNKNOWN", 5)
        self.assertFalse(success)
        self.assertNotIn("UNKNOWN", self.tracker.portfolio)

    def test_add_stock_negative_or_zero_quantity(self):
        success, msg = self.tracker.add_stock("AAPL", 0)
        self.assertFalse(success)
        success, msg = self.tracker.add_stock("AAPL", -5)
        self.assertFalse(success)

    def test_add_stock_cumulative(self):
        self.tracker.add_stock("AAPL", 5)
        self.tracker.add_stock("AAPL", 10)
        self.assertEqual(self.tracker.portfolio["AAPL"], 15)

    def test_calculate_total_investment(self):
        # AAPL price = 180, TSLA price = 250
        # 10 * 180 = 1800
        # 2 * 250 = 500
        # Total = 2300
        self.tracker.add_stock("AAPL", 10)
        self.tracker.add_stock("TSLA", 2)
        total = self.tracker.calculate_total_investment()
        self.assertEqual(total, 2300.0)

    def test_remove_stock(self):
        self.tracker.add_stock("MSFT", 4)
        self.assertIn("MSFT", self.tracker.portfolio)
        success, msg = self.tracker.remove_stock("MSFT")
        self.assertTrue(success)
        self.assertNotIn("MSFT", self.tracker.portfolio)

    def test_save_to_txt(self):
        self.tracker.add_stock("AAPL", 10)
        self.tracker.add_stock("GOOGL", 5)
        txt_path = self.tracker.save_to_txt("test_portfolio.txt")
        self.assertTrue(os.path.exists(txt_path))
        with open(txt_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("AAPL", content)
            self.assertIn("GOOGL", content)
            self.assertIn("TOTAL PORTFOLIO INVESTMENT VALUE", content)
        if os.path.exists(txt_path):
            os.remove(txt_path)

    def test_save_to_csv(self):
        self.tracker.add_stock("AAPL", 10)
        self.tracker.add_stock("GOOGL", 5)
        csv_path = self.tracker.save_to_csv("test_portfolio.csv")
        self.assertTrue(os.path.exists(csv_path))
        with open(csv_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Ticker,Quantity,Price_USD,Total_Value_USD", content)
            self.assertIn("AAPL,10.0,180.0,1800.0", content)
        if os.path.exists(csv_path):
            os.remove(csv_path)


if __name__ == "__main__":
    unittest.main()
