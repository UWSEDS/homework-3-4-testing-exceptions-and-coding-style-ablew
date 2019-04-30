"""Unit tests for the dataframe module"""

import unittest
import dataframe


def test_rows(data_frame):
    """
    Checks that the dataframe has more than 1 row.
    :params dataframe df:
    :returns bool:
    """
    nrows = len(data_frame)
    one_row = True
    if nrows < 1:
        one_row = False
    return one_row

def test_columns(data_frame):
    """
    Checks that the dataframe has the required columns.
    :params dataframe data_frame:
    :returns bool:
    """
    required_columns = True
    cols = list(data_frame)
    for col in cols:
        if col not in ['Draw Date', 'Winning Numbers', 'Mega Ball', 'Multiplier']:
            required_columns = False
            break
        else:
            pass
    return required_columns

def add_wrong_column(data_frame):
    """
    Adds wrong column to dataframe
    :params dataframe data_frame:
    :returns dataframe:
    """
    new_df = data_frame.copy()
    new_df['Ducks'] = 0
    return new_df

def test_winning_numbers(data_frame):
    """
    Checks that there are 5 winning numbers in the 'Winning Numbers' column
    :params dataframe data_frame:
    :returns bool:
    """
    five_numbers = True
    for i in range(len(data_frame)):
        numbers = len(dataframe.DF.iloc[i, 1].split())
        if numbers != 5:
            five_numbers = False
            break
        else:
            pass
    return five_numbers

class UnitTests(unittest.TestCase):
    """
    Class for unit testing
    """

    def test_success(self):
        """
        Unit test for number of columns.
        """
        self.assertTrue(test_columns(dataframe.DF))

    def test_success1(self):
        """
        Unit test for number of rows.
        """
        self.assertTrue(test_rows(dataframe.DF))

    def test_success2(self):
        """
        Unit test for number of winning numbers.
        """
        self.assertTrue(test_winning_numbers(dataframe.DF))

    def test_failure(self):
        """
        Unit test to check if test_columns can fail.
        """
        self.assertFalse(test_columns(add_wrong_column(dataframe.DF)))

SUITE = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(SUITE)
