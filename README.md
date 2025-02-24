# Stock Difference Calculator

## Description
This script will loop through all symbols in the NASDAQ, calculate the difference on close from the first and last day, then dump those values into a CSV for analysis. 

## How to Run
1. Ensure you have the latest data: ftp://ftp.nasdaqtrader.com/SymbolDirectory/ or https://www.nasdaq.com/market-activity/stocks/screener

2. Update variables to match your query:
```
STARTYEAR
STARTMONTH
STARTDAY

ENDYEAR
ENDMONTH
ENDDAY

SOURCE_FILE
```

3. Ensure `singleSymbol=line.split(',')[0]` is updated to match your splitting characterp

4. `python .\app`

## Data Source

FTP Mirror: ftp://ftp.nasdaqtrader.com/SymbolDirectory/
Backup: https://www.nasdaq.com/market-activity/stocks/screener (download as CSV)

Symbol Look-Up/Directory Data Fields & Definitions: http://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs#nasdaq