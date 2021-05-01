import yfinance as yf # https://pypi.org/project/yfinance/
import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr 
import os.path as path

# Update these veriables below to scope your query 
STARTYEAR=2020
STARTMONTH=1
STARTDAY=1

ENDYEAR=2021
ENDMONTH=4
ENDDAY=30

SOURCE_FILE='allsymbols.txt'
# Update variables above to scope your query

SYMBOLS = []
PROBLEMLIST = []

start=dt.datetime(STARTYEAR,STARTMONTH,STARTDAY)
end=dt.datetime(ENDYEAR,ENDMONTH,ENDDAY)

# Gather all stock symbols from data file
for line in open('src\\{}'.format(SOURCE_FILE)): # Change this 
  singleSymbol=line.split(',')[0] #! Keep an eye out for the splitting character in your src document, this may change
  SYMBOLS.append(singleSymbol)

# Remove 'Symbol' and 'file created ...'
SYMBOLS=SYMBOLS[1:-1]

# Create dataframe to hold totalDifference values
trackingDF = pd.DataFrame(columns=['Stock','totalDifference','Start','End'])

trackingCount = 0

for symbol in SYMBOLS:
  trackingCount += 1
  try:
    print('--- {} of {} ---'.format(trackingCount,len(SYMBOLS)))
    df=pdr.get_data_yahoo(symbol,start,end)
    startValue = df['Close'][0] # First closing price
    endValue = df['Close'][-1] # Last closing price 
    totalDifference = endValue - startValue
    # This will make it so only stocks that still haven't recovered are tracked
    if totalDifference < 0:
      new_row = {'Stock':symbol,'totalDifference':totalDifference,'Start':startValue,'End':endValue}
      trackingDF = trackingDF.append(new_row,ignore_index=True)
  except:
    print('Problem with {}'.format(symbol))
    PROBLEMLIST.append(symbol)

# export to a CSV
trackingDF.to_csv(f'.\\output\\{STARTMONTH}-{STARTMONTH}-{STARTDAY} to {ENDMONTH}-{ENDDAY}-{ENDYEAR}.csv', index=False)