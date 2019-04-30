import pandas as pd

df = pd.read_csv("https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD")

print("The dataframe has %d columns." % len(list(df)))

def test_create_dataframe(df):
    checks = []
    
    if list(df) == ['Draw Date', 'Winning Numbers', 'Mega Ball', 'Multiplier']:
        checks.append(1)
    else:
        checks.append(0)
    
    types = []
    
    for i in range(len(list(df))):
        types.append(str(df[list(df)[i]].dtypes))
        
    if types == ['object', 'object', 'int64', 'float64']:
        checks.append(1)
    else:
        checks.append(0)
        
    if len(df) >= 10:
        checks.append(1)
    else:
        checks.append(0)
        
    if sum(checks) == 3:
        return True
    else:
        return False
    
