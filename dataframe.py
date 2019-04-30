"""Imports the module from hw2, reads the dataframe and raises error if the columns don't match."""

import hw2

DF = hw2.df

for col in list(DF):
    if col not in ['Draw Date', 'Winning Numbers', 'Mega Ball', 'Multiplier']:
        raise ValueError("DataFrame should have a column named '%s'." % col)
