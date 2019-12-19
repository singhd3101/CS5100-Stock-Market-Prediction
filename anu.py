import quandl
# pandas for data manipulation

import pandas as pd
quandl.ApiConfig.api_key = 'YDotLd6LN2sn-XsEtygx'
# Retrieve TSLA data from Quandl
tesla = quandl.get('WIKI/TSLA')
dftesla = pd.DataFrame(tesla)


dftesla.to_csv('tesla.csv')
print(dftesla)
