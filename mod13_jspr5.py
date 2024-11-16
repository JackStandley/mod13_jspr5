import unittest
from datetime import datetime

class TestInputs(unittest.TestCase):
    def test_dates(self):
        def is_valid_date(date_text):
            if len(date_text) != 10 or date_text[4] != '-' or date_text[7] != '-':
                return False
            try:
                datetime.strptime(date_text, "%Y-%m-%d")
                return True
            except ValueError:
                return False

    
        valid_dates = ["2023-01-01", "2020-12-31"]

        invalid_dates = ["2023/01/01", "01-01-2023", "2023-1-1", "20231301", ""]

        for date in valid_dates:
            self.assertTrue(is_valid_date(date), f"{date} should be valid")

        for date in invalid_dates:
            self.assertFalse(is_valid_date(date), f"{date} should be invalid")

    def test_symbol(self):
        valid_symbols = ["AAPL", "MSFT", "GOOGL"]
        invalid_symbols = ["aapl", "123", "GOOGLE123", ""]

        for symbol in valid_symbols:
            self.assertTrue(symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7)

        for symbol in invalid_symbols:
            self.assertFalse(symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7)

    def test_chart_type(self):
        valid_chart_types = ["1", "2"]
        invalid_chart_types = ["3", "10", "a", "", "12"]

        for chart_type in valid_chart_types:
            self.assertIn(chart_type, ["1", "2"])

        for chart_type in invalid_chart_types:
            self.assertNotIn(chart_type, ["1", "2"])

    def test_time_series(self):
        valid_time_series = ["1", "2", "3", "4"]
        invalid_time_series = ["0", "5", "10", "a", ""]

        for time in valid_time_series:
            self.assertIn(time, ["1", "2", "3", "4"])

        for time in invalid_time_series:
            self.assertNotIn(time, ["1", "2", "3", "4"])

if __name__ == "__main__":
    unittest.main()
